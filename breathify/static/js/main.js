
let counter1 = 0
function counter(){
    counter1++;
    const headingSelector = document.querySelector('h2');
    headingSelector.innerHTML = counter1 
}

document.addEventListener('DOMContentLoaded', ()=> {
    document.querySelector('button').onclick = counter;
    document.querySelector('form').onsubmit = ()=> {
        const name = document.querySelector('#name').value;
        alert(`hello, ${name} your token is ${counter1}!`)
    }

    document.querySelectorAll('button').forEach((button)=>{
        button.onclick = ()=> {
            document.querySelector('h1').style.color = button.dataset.color;
        }
 

    })
})