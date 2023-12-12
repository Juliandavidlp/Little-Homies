
const { createApp } = Vue;
createApp({
  data() {
    return {
        mascotas : [],
        api_server:"http://127.0.0.1:8000",
        id:'',
        title:'',
        descripción:'',
        año_de_nacimiento:'',
        banner:null
    };
  },
  methods: {

    getMascotas() { // Metodo para buscar las mascotas en el servidor
        fetch(`${this.api_server}/api/mascotas/`)
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
                this.mascotas = data;
            })
            .catch((err) => {
                console.error(err);
            });
    },
    getMascota(id_mascota) {
        fetch(`${this.api_server}/api/mascotas/${id_mascota}/`, {
            method: 'GET',
        })
        .then((response) => response.json())
        .then((data) => {
            this.id_mascota = data.id;
            this.title = data.title;
            this.descripción = data.descripción,
            this.año_de_nacimiento = data.año_de_nacimiento
            console.log(data);
        })
        .catch((error) => {
            console.error("Error al enviar el formulario:", error);
        });
    },
    
},
  created() {
    this.getMascotas();
  },
}).mount("#app");
