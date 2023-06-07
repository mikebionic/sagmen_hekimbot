$(document).ready(function () {
	$("body").delegate("#addDrugsRowButton", "click", function (e) {
		const payload = {
			note: $("#manage_drug_note").val(),
			name: $("#manage_drug_name").val(),
			hex: $("#manage_drug_hex").val(),
			qty: $("#manage_drug_qty").val(),
			unit: $("#manage_drug_unit").val(),
		};
		if (payload.name.length > 0) {
			console.log(payload)
			post_drugs(payload);
			$("#addDrugsRowModal").modal("hide");
		}
	});
});

$("body").delegate(".newDataModalBtn", "click", function(e) {
	$("#manage_drug_note").val("")
	$("#manage_drug_name").val("")
	$("#manage_drug_hex").val("")
	$("#manage_drug_qty").val("")
	$("#manage_drug_unit").val("")
})

const post_drugs = async (payload) => {
	var config = {
		method: "POST",
		headers: { "Content-Type": "Application/json" },
		body: JSON.stringify(payload),
	};
	const data = await fetch("/manage_drugs/", config).then((response) =>
		response.json()
	);
	console.log(data, data.status)
	if (data.status == 1){
		$('.drug_table_rows').prepend(construct_drug_table_row(data.data));
	}
	else if (data.status == 2){
		$(`.item_row[owner_id="drug_${data.data.hex}"]`).remove();
		$('.drug_table_rows').prepend(construct_drug_table_row(data.data));
	}
};

const delete_drug = async (payload) => {
	console.log(payload)
	var config = {
		method: "POST",
		headers: { "Content-Type": "Application/json" },
		body: JSON.stringify(payload),
	};
	const data = await fetch("/manage_drugs/?delete=1", config).then((response) =>
		response.json()
	);
	console.log(data)
	if (data.status !== 0){
		$(`.item_row[owner_id="drug_${data.data.hex}"]`).remove();
	}
}

$("body").delegate(".remove_btn", "click", function (e) {
	delete_drug({
		hex: $(this).attr("owner_id").split("_")[1]
	})
	// $(`.item_row[owner_id="${$(this).attr("owner_id")}"]`).remove();
});

$("body").delegate(".edit_btn", "click", function (e) {
	$("#manage_drug_note").val(
		$(`.item_row[owner_id="${$(this).attr("owner_id")}"] .note`).html()
	)
	$("#manage_drug_name").val(
		$(`.item_row[owner_id="${$(this).attr("owner_id")}"] .name`).html()
	)
	$("#manage_drug_hex").val($(this).attr("owner_id").split("_")[1])
	$("#manage_drug_qty").val(
		$(`.item_row[owner_id="${$(this).attr("owner_id")}"] .qty`).html()
	)
	$("#manage_drug_unit").val(
		$(`.item_row[owner_id="${$(this).attr("owner_id")}"] .unit`).html()
	)

	$("#addDrugsRowModal").modal("show");
	// $('.item_row[owner_id=drug_5fc72f800e5e25d59466b5962] .name')
});


const construct_drug_table_row = (
	data
) => `<tr class="item_row" owner_id="drug_${data.hex}">
	<td class="text-center name">${data.name}</td>
	<input type="hidden" class="hex" value="${data.hex}" />
	<td class="text-center unit">${data.unit}</td>
	<td class="text-center qty">${data.qty}</td>
	<td class="text-center note">${data.note}</td>
	<td class="text-center">
		<div class="form-button-action">
			<button
				type="button"
				data-toggle="tooltip"
				title=""
				class="btn btn-link btn-primary btn-lg edit_btn"
				owner_id="drug_${data.hex}"
			>
				<i class="icofont-edit"></i>
			</button>
			<button
				type="button"
				data-toggle="tooltip"
				title=""
				class="btn btn-link btn-danger remove_btn"
				owner_id="drug_${data.hex}"
			>
				<i class="icofont-bin"></i>
			</button>
		</div>
	</td>
</tr>`;
