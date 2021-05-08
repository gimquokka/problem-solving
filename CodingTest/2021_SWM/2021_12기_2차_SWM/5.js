function DarkMode() {
    const $cb = document.querySelector('darkModeSwitch')
    
    $cb.addEventListener('click', e => {
        // if (e.target.checked) {
        //     document.documentElement.setAttribute('color-theme', dark);
        // } else {
        //     document.documentElement.setAttribute('color-theme', "light");
        // }
        console.log(e)
    })
}