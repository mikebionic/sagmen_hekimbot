// 1 get Person (people) to fetch name by ID or make a select menu
// 2 get curing records

$(document).ready(function () {
	$("body").delegate("#addHospital_recordRowButton", "click", function (e) {
		const payload = {
			note: $("#manage_hospital_record_note").val(),
			name: $("#manage_hospital_record_name").val(),
			hex: $("#manage_hospital_record_hex").val(),
			qty: $("#manage_hospital_record_qty").val(),
			unit: $("#manage_hospital_record_unit").val(),
		};
		if (payload.name.length > 0) {
			console.log(payload);
			post_hospital_records(payload);
			$("#addHospital_recordRowModal").modal("hide");
		}
	});
});

$("body").delegate(".newDataModalBtn", "click", function (e) {
	$("#manage_hospital_record_note").val("");
	$("#manage_hospital_record_name").val("");
	$("#manage_hospital_record_hex").val("");
	$("#manage_hospital_record_qty").val("");
	$("#manage_hospital_record_unit").val("");
});

const post_hospital_records = async (payload) => {
	var config = {
		method: "POST",
		headers: { "Content-Type": "Application/json" },
		body: JSON.stringify(payload),
	};
	const data = await fetch("/manage_hospital_records/", config).then(
		(response) => response.json()
	);
	console.log(data, data.status);
	if (data.status == 1) {
		$(".hospital_record_table_rows").prepend(
			construct_hospital_record_table_row(data.data)
		);
	} else if (data.status == 2) {
		$(`.item_row[owner_id="hospital_record_${data.data.hex}"]`).remove();
		$(".hospital_record_table_rows").prepend(
			construct_hospital_record_table_row(data.data)
		);
	}
};

const delete_hospital_record = async (payload) => {
	// console.log(payload)
	var config = {
		method: "POST",
		headers: { "Content-Type": "Application/json" },
		body: JSON.stringify(payload),
	};
	const data = await fetch("/manage_hospital_records/?delete=1", config).then(
		(response) => response.json()
	);
	console.log(data);
	if (data.status !== 0) {
		$(`.item_row[owner_id="hospital_record_${data.data.hex}"]`).remove();
	}
};

$("body").delegate(".remove_btn", "click", function (e) {
	delete_hospital_record({
		hex: $(this).attr("owner_id").split("_")[1],
	});
	// $(`.item_row[owner_id="${$(this).attr("owner_id")}"]`).remove();
});

$("body").delegate(".edit_btn", "click", function (e) {
	$("#manage_hospital_record_note").val(
		$(`.item_row[owner_id="${$(this).attr("owner_id")}"] .note`).html()
	);
	$("#manage_hospital_record_name").val(
		$(`.item_row[owner_id="${$(this).attr("owner_id")}"] .name`).html()
	);
	$("#manage_hospital_record_hex").val($(this).attr("owner_id").split("_")[1]);
	$("#manage_hospital_record_qty").val(
		$(`.item_row[owner_id="${$(this).attr("owner_id")}"] .qty`).html()
	);
	$("#manage_hospital_record_unit").val(
		$(`.item_row[owner_id="${$(this).attr("owner_id")}"] .unit`).html()
	);

	$("#addHospital_recordRowModal").modal("show");
	// $('.item_row[owner_id=hospital_record_5fc72f800e5e25d59466b5962] .name')
});

const construct_hospital_record_table_row = (data) => `
	<tr class="item_row" owner_id="hospital_record_${data.hex}">
		<td class="text-center name">${data.m_level}</td>
		<input type="hidden" class="hex" value="${data.hex}" />
		<input type="hidden" class="hospital_id" value="${data.hospital_id}" />
		<td class="text-center m_level">${data.m_level}</td>
		<td class="text-center enter_date">${data.enter_date}</td>
		<td class="text-center exit_date">${data.exit_date}</td>

		<td class="text-center completed">checkbox</td>
		<td class="text-center reason">reason</td>
		<td class="text-center completed">checkbox</td>
		<td class="text-center">
			<div class="form-button-action">
				<button
					type="button"
					data-toggle="tooltip"
					title=""
					class="btn btn-link btn-primary btn-lg edit_btn"
					owner_id="hospital_record_{{item.hex}}"
				>
					<i class="icofont-edit"></i>
				</button>
				<button
					type="button"
					data-toggle="tooltip"
					title=""
					class="btn btn-link btn-danger remove_btn"
					owner_id="hospital_record_{{item.hex}}"
				>
					<i class="icofont-bin"></i>
				</button>
			</div>
		</td>
	</tr>
`;
