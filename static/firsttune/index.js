window.onload = (event) => {
    fadeIn()

    setTimeout(remove, 2500)
    hide_wait_small()
    setTimeout(show_wait_small, 2000)


}

fadeIn =() => {
    homerow = document.getElementById('homepic')
    console.log(homerow)
    homerow.classList.add("animate__animated")
    homerow.classList.add("animate__slower")

    homerow.classList.add("animate__fadeOut")

}

remove = () => {
    homerow = document.getElementById('homepic')

    homerow.classList.add("d-none")

}

hide_wait_small = ( ) => {
    wait_small  = document.getElementById('wait_small')
    wait_small.classList.add('d-none')
}

show_wait_small = () => {
    wait_small  = document.getElementById('wait_small')
    wait_small.classList.add('d-block')
}