const submitForm = async () => {

    const query = document.querySelector('#search-query')
    console.log(query)

    let response = await fetch(`http://localhost:8000/search/?query=${query.target.value}`)

}

let btn = document.querySelector('#submitbtn')
console.log(btn)


btn.addEventListener('click', () => {
    const query = document.querySelector('#search-query')
    console.log(query)
})