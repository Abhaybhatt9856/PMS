const sidebar=document.querySelector('.sidebar');
const togglebtn=document.querySelector('.toggle-btn');

togglebtn.addEventListener('click', () =>{
    sidebar.classList.toggle('active');
});