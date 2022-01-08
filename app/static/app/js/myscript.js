/**
 * @Author: Your name
 * @Date:   2022-01-06 11:11:50
 * @Last Modified by:   Your name
 * @Last Modified time: 2022-01-06 18:03:55
 */
$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})