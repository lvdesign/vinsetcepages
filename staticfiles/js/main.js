console.log('heello');
/*
// voir aussi https://www.a11ymatters.com/pattern/mobile-nav/
// Nav action
const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-list");

hamburger.addEventListener("click", mobileMenu);

function mobileMenu() {
    hamburger.classList.toggle("active");
    navMenu.classList.toggle("active");
}

const navLink = document.querySelectorAll(".nav-link");

navLink.forEach(n => n.addEventListener("click", closeMenu));

function closeMenu() {
    hamburger.classList.remove("active");
    navMenu.classList.remove("active");
}
*/
// Rotation image

(function(){
    "use strict";    
        let counter=1;    
        function contentRotator(){    
            $(`#my_rotator figure:nth-child(${counter})`).fadeIn( 2000, function(){ // retour au debut
                    if( $(this).is("#my_rotator figure:last-child") ){
                        setTimeout( function(){
                            $(`#my_rotator figure:nth-child(${counter})`).fadeOut( 2000, function(){
                                counter=1;
                                contentRotator()
                            });    
                        },3000)   
    
                    }else{
                        setTimeout( function(){
                            $(`#my_rotator figure:nth-child(${counter})`).fadeOut( 2000, function(){
                                counter++;
                                contentRotator()
                            });
                        },3000 );
                    }
                });
        }    
        contentRotator();
    }())

    /*
    (function(){
        "use strict";
        
            let counter=1;
        
            function contentRotator(){
        
                $(`#my_rotator_region figure:nth-child(${counter})`).fadeIn( 2000, function(){ // retour au debut
                        if( $(this).is("#my_rotator_region figure:last-child") ){
                            setTimeout( function(){
                                $(`#my_rotator_region figure:nth-child(${counter})`).fadeOut( 2000, function(){
                                    counter=1;
                                    contentRotator()
                                });
        
                            },3000)
        
        
                        }else{
                            setTimeout( function(){
                                $(`#my_rotator_region figure:nth-child(${counter})`).fadeOut( 2000, function(){
                                    counter++;
                                    contentRotator()
                                });
                            },2000 );
                        }
                    });
            }    
            contentRotator();
        
        
        }());
        */