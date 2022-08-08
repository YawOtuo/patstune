window.onload = (event) => {
    fadeIn()

    setTimeout(slideOut, 2500)
    // setTimeout(slideOut, 2500)

    // hide_wait_small()
    // setTimeout(show_wait_small, 1500)


}

fadeIn =() => {
    homerow = document.getElementById('homepic')
    console.log(homerow)
    homerow.classList.add("animate__animated")
    homerow.classList.add("animate__slow")

    homerow.classList.add("animate__fadeIn")

}

slideOut = () => {
    homerow = document.getElementById('homepic')
    console.log(homerow)
    homerow.classList.add("animate__animated")
    homerow.classList.add("animate__slow")

    // homerow.classList.add("animate__slideOutUp")  

    // homerow.classList.add('d-none')
}

remove = () => {
    homerow = document.getElementById('homepic')
    homerow.classList.add('d-none')

}

hide_wait_small = ( ) => {
    wait_small  = document.getElementById('wait_small')
    wait_small.classList.add('d-none')
}

show_wait_small = () => {
    wait_small  = document.getElementById('wait_small')
    wait_small.classList.add('d-block')
}