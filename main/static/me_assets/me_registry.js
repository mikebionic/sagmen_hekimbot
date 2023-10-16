$(".new_registry_btn").click(function (e) {
	$("[name=user_fullname]").val("");
	$("[name=title]").val("");
	$("[name=description]").val("");
	$("[name=registry_date]").val("");
	$("[name=time_str]").val("");

	console.log();
	$(`.me_addregistry`).hide("fast");
	$(`.me_addregistry[owner_id=${$(this).attr("owner_id")}]`).show("slow");
});

$(".save_registry_btn").click(function (e) {
	var owner_id = $(this).attr("owner_id");
	var payload = {
		doctor_id: owner_id,
		user_fullname: $(`[name=user_fullname][owner_id=${owner_id}]`).val(),
		title: $(`[name=title][owner_id=${owner_id}]`).val(),
		description: $(`[name=description][owner_id=${owner_id}]`).val(),
		registry_date: $(`[name=registry_date][owner_id=${owner_id}]`).val(),
		time_str: $(`[name=time_str][owner_id=${owner_id}]`).val(),
	};
	if (
		payload["user_fullname"].length < 1 ||
		payload["title"].length < 1 ||
		payload["registry_date"].length < 1 ||
		payload["user_fullname"].length < 1 ||
		payload["time_str"].length < 1
	) {
		console.log("record data none");
	} else {
		console.log(payload);
		$(`.me_addregistry`).hide("fast");
		post_registry(payload);
	}
});

$("body").delegate(".newDataModalBtn", "click", function (e) {});

const post_registry = async (payload) => {
	var config = {
		method: "POST",
		headers: { "Content-Type": "Application/json" },
		body: JSON.stringify(payload),
	};
	const data = await fetch("/manage_registry/", config).then((response) =>
		response.json()
	);
	console.log(data, data.status);
	if (data.status == 1) {
		$(`.registry_records`).prepend(construct_registry_row(data.data));
	}
	// else if (data.status == 2) {
	// 	$(`.item_row[owner_id="drug_${data.data.hex}"]`).remove();
	// 	$(".drug_table_rows").prepend(construct_registry_row(data.data));
	// }
};

const construct_registry_row = (data) =>
	`
	<div class="row" style="justify-content: space-between; align-items: center; margin:.5rem;box-shadow: 0px 0px 15px #a3c7e96e;">
		<div class="col-8">
			<p owner_id="${data.doctor_id}" class="reg_hex" style="display:none">${data.hex}</p>
			<b owner_id="${data.doctor_id}" class="reg_user_fullname">${data.user_fullname}</b>
			<p owner_id="${data.doctor_id}" class="reg_title">${data.title}</p>
		</div>
		<div class="col-4" style="font-size: smaller;">
			<b owner_id="${data.doctor_id}" class="reg_registry_date">${data.registry_date} ${data.time_str}</b>
			<p owner_id="${data.doctor_id}" class="reg_status" style="color:${data.color}">${data.status}</p>
		</div>
	</div>
`;

$(".me_registry_accept").click(function (e) {
	post_registry({
		hex: $(this).attr("hex"),
		status: "accepted",
	});
});

$(".me_registry_cancel").click(function (e) {
	post_registry({
		hex: $(this).attr("hex"),
		status: "declined",
	});
});
$(".me_registry_delete").click(function (e) {
	post_registry({
		hex: $(this).attr("hex"),
		deleted: 1,
	});
});

const me_notify_swal = (data) => {
	swal({
		// timer: 6000,
		title: data.user_fullname,
		text: `${data.title}\n${data.description}`,
		type: "info",
		icon: "info",
		buttons: {
			accept: {
				text: "Kabul et!",
				className: "btn btn-success",
			},
			cancel: {
				text: "Terk et!",
				visible: true,
				className: "btn btn-danger",
			},
		},
	}).then(function (ok) {
		if (ok) {
			post_registry({
				hex: data.hex,
				status: "accepted",
			});
			swal("Kabul edildi!", {
				icon: "success",
				timer: 2000,
				buttons: {
					confirm: {
						className: "btn btn-success",
					},
				},
			});
		} else {
			post_registry({
				hex: data.hex,
				status: "declined",
			});
			swal("Terk edildi!", {
				icon: "warning",
				timer: 2000,
				buttons: {
					confirm: {
						className: "btn btn-success",
					},
				},
			});
		}
	});
};

var doctor_id = $("#doctor_id").val();
console.log(doctor_id);
var recovery = {};
var new_rec;
setInterval(async () => {
	var config = {
		method: "GET",
	};
	if (doctor_id) {
		const data = await fetch(`/get_latest_registry/${doctor_id}`, config).then(
			(response) => response.json()
		);
		console.log(recovery, data.data);
		if (recovery != data.data) {
			if (recovery != {}) {
				new_rec = 1;
			}
			recovery = data.data;
			if (new_rec == 1) {
				me_notify_swal(recovery[0]);
			}
		} else {
			new_rec = 0;
		}
	}
}, 500);
