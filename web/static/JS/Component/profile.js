
const navLiProfile = () => {
  
    const liPro = document.querySelectorAll('div#submenu-profile  ul  button');
    liPro.forEach((li) =>
    li.addEventListener('click', function (e) {
          
   liPro.forEach((x) => (x.className = 'list-group-item list-group-item-warning list-group-item-action'));
        document.querySelector(`#submenu-profile > ul  button[name="${e.target.name}"]`).className =
        'list-group-item list-group-item-warning list-group-item-action active';
    })
    );
};
const configButtonProfile = ()=>{

    document.querySelector(`div#submenu-profile ul button[name="configuracion"]`).addEventListener('click', function (e) 
    { 
        document.getElementById('content-profile').style.display = "none";
        document.getElementById('content-profile2').style.display = "block";  
    })
    document.querySelector(`div#submenu-profile ul button[name="perfil"]`).addEventListener('click', function (e) 
    { 
        document.getElementById('content-profile').style.display = "block";
            
        document.getElementById('content-profile2').style.display = "none";  

    })
}

function profileFn(){
    navLiProfile();
    configButtonProfile();
}