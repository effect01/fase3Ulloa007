function RegLogState(bin) {
  this.state = bin;
}
let stat = new RegLogState(false);

const changeOnClick = (bin) => {
  stat.state = bin;
};

// invalid= { this.validationStr(this.state.displayName)  }  valid={ false}
const submitLogin = () => {
  stat.state;
};

const onchangg = (e) => {
  let trig;
  if (e.name) {
    switch (e.name) {
      case 'email' || 'email1':
        trig = verify.emailCharacter(e.value);
        break;
      case 'username':
        trig = verify.lengthAndCharacter(e.value, 3, 25);
        break;
      case 'password' || 'password1':
        trig =
          verify.cap(e.value) && verify.lengthAndCharacter(e.value, 5, 25)
            ? true
            : false;
        break;
      case 'password2':
        trig =
          verify.equalString(
            e.value,
            document.querySelector('input[name="password"]').value
          ) === 0
            ? true
            : false;
        break;
      default:
        console.log('name.error in input tag');
    }

    trig
      ? (document.querySelector(`#id_'${e.name}']`).className =
          'form-control is-valid')
      : (document.querySelector(`#id_'${e.name}']`).className =
          'form-control is-invalid');
  }
};

const fixedLogin = () => {
  const listLabelName = {
    div_id_username: 'Nombre de usuario',
    div_id_email: 'Correo',
    div_id_password: 'Contraseña',
    div_id_password1: 'Contraseña',
    div_id_password2: 'Ingrese nuevamente la contraseña',
    div_id_first_name: 'Nombre',
    div_id_last_name: 'Apellido',
    div_id_dateBirth: 'Fecha de cumpleaños :)',
    div_id_code_number: "Codigo de Telefono",
    div_id_phone_number: "Numero de Celular",
    div_id_image: 'Inserte una imagen',
    div_id_comment: 'Deja tu comentario !',
    div_id_title: 'Titulo',
    div_id_content: 'Contenido',
    div_id_genre: 'Genero',
    div_id_author:'Autor',
    div_id_previewContent:'Contenido previo',
    div_id_year: 'Años en que se publico',
    div_id_publisher: "Publicador de la edicion",
    div_id_country: "Pais",
    div_id_base_price: "Precio base"

  };


  for (const [key, value] of Object.entries(listLabelName)) {
    const element = key;
    if (document.querySelector(`#${element}`)) {
      let placeHolder = value;
      let idIn = element.substring(4, element.length);
      newStyleForm(element,value);
      translateInput(idIn, placeHolder);
    }
  }
};



const newStyleForm = (inputGroupId,name) => {
  let isText = false;
  const listYesLabel = ["div_id_phone_number" , "div_id_code_number",  "div_id_image", 'div_id_dateBirth',
  'div_id_title',
  'div_id_content',
  'div_id_genre',
  'div_id_author',
  'div_id_previewContent',
  'div_id_year',
  'div_id_publisher',
  'div_id_country',
  'div_id_base_price',]
  listYesLabel.forEach(
  names =>{
    if(inputGroupId ==  names ){
      document.querySelector(`#${inputGroupId} label`).textContent= name ;
      isText = true;
    }
  })
 if(!isText){
    document.querySelector(`#${inputGroupId} label`).style.display = 'none';
  }
  document.querySelector(`#${inputGroupId}`).style.marginTop = '20px';


};



const translateInput = (id, newName) => {
  document.querySelector(`#${id}`).placeholder =
    newName.replace(/^\w/, c => c.toUpperCase());;
  // document.querySelector(`#${idIn}`).onchange = ()=> onchangg();
};

window.addEventListener('load', () => {
  fixedLogin();
});
