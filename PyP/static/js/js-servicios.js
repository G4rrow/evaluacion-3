$(document).ready(function () {
    //GET
    $.ajax({
        url: "https://reqres.in/api/users?page=2",
        type: "GET",
        data: {},
        dataType: 'json',
        success: function (response) {
            response.data.forEach((persona, index) => {
                //console.log(index, persona)
                if (index == 0) {
                    $("#carrusel-items").append(
                        `<div class="carousel-item active">
                        <div class="row">
                        <div class="col-md-12 mb-3">
                            <div class="card-trabajador">
                            <img src=${persona.avatar} alt="" class="img-trabajador">
                            <div class="info">
                                <div class="info-nombre">
                                ${persona.first_name} ${persona.last_name}
                                </div>
                                <div class="info-correo">
                                ${persona.email}
                                </div>
                            </div>
                            </div>
                        </div>
                        </div>
                    </div>`
                    );
                } else {
                    $("#carrusel-items").append(
                        `<div class="carousel-item">
                        <div class="row">
                        <div class="col-md-12 mb-3">
                            <div class="card-trabajador">
                            <img src=${persona.avatar} alt="" class="img-trabajador">
                            <div class="info">
                                <div class="info-nombre">
                                ${persona.first_name} ${persona.last_name}
                                </div>
                                <div class="info-correo">
                                ${persona.email}
                                </div>
                            </div>
                            </div>
                        </div>
                        </div>
                    </div>`
                    );
                }
            });
        }
    });

});