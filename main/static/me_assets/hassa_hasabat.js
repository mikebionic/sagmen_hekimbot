
let api_prefix = "";
let api_port = "5300";
let get_curing_url = `${location.protocol}//${location.hostname}:${api_port}${api_prefix}/curing_records/`;
let get_in_loc_clinic_url = `${location.protocol}//${location.hostname}:${api_port}${api_prefix}/in_local_clinic/`;

const get_curing_async = async () => {
    return await fetch(get_curing_url, {
        method:"GET", 
        credentials:'include',
        // headers: {Authorization: `Basic ${auth}`, u_type: u_type}
    }).then(response => response.json())
}
const get_in_loc_clinic_async = async () => {
    return await fetch(get_in_loc_clinic_url, {
        method:"GET", 
        credentials:'include',
        // headers: {Authorization: `Basic ${auth}`, u_type: u_type}
    }).then(response => response.json())
}


const curing_ui = async () => {
    let data = await get_curing_async();
    await $(".hassa_hasabat_circles div").remove()
    data.data.map((item) => {
        if (!item.deleted){
            $(".hassa_hasabat_circles").append(create_circle_layer(item))
            Circles.create({
                id: `circles-${item.id}${item.hex}`,
                radius: 45,
                value: item.qty,
                maxValue: item.maxval,
                width: 7,
                text: item.qty || "0",
                colors: ["#f1f1f1", item.color_code],
                duration: 400,
                wrpClass: "circles-wrp",
                textClass: "circles-text",
                styleWrapper: true,
                styleText: true,
            });
        }
    })
}

curing_ui()
setInterval(() => {
    curing_ui()
}, 6000);

const create_circle_layer = (item) => {
    return `
    <a href="${hospital_rec_url}?id=${item.id}">
        <div class="px-2 pb-2 pb-md-0 text-center">
            <div id="circles-${item.id}${item.hex}"></div>
            <h6 class="fw-bold mt-3 mb-0">${item.name}</h6>
        </div>
    </a>
    `
}

///////////////////////

const loc_clinic_ui = async () => {
    let data = await get_in_loc_clinic_async();
    await $(".me_loc_clinic_list div").remove()
    data.data.map((item) => {
        $(".me_loc_clinic_list").append(create_person_badge(item))
    })
    // console.log(data)
}

loc_clinic_ui()
setInterval(() => {
    loc_clinic_ui()
}, 6000);

// ${item.name[0].upper() if item.name else
//     '.'}${item.surname[0].upper() if item.surname else
//     '.'}
const create_person_badge = (item) => {
    return `
    <div class="col-md-12 col-lg-6 d-flex" style="align-items: center">
        <div class="avatar avatar-sm">
            <span class="avatar-title rounded-circle border border-white"
                >
                ${ item.name ? item.name[0].toUpperCase() : "." }${ item.surname ? item.surname[0].toUpperCase() : "." }
                </span
            >
        </div>
        <div class="flex-1 row">
            <div class="col">${item.name} ${item.surname}</div>
            <div class="col float-right" style="flex-direction: column">
                <small class="text-muted">${item.created_date}</small>
                <span class="text-warning pl-3">${item.m_level}</span>
            </div>
        </div>
    </div>
    `
}
