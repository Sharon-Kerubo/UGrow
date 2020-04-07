            $(document).ready(function(){
                $('.menu-toggle').click(function(){
                    $('nav').toggleClass('active')
                })
                $('ul li').click(function(){
                    $(this).siblings().removeClass('active');
                    $(this).toggleClass('active');
                })
            })

            document.getElementById("logn").addEventListener("click", function(){
                document.querySelector(".popup").style.display = "flex";
            })
            document.querySelector(".close").addEventListener("click", function(){
                document.querySelector(".popup").style.display = "none";
            })

            document.getElementById("btn").addEventListener("click", function(){
                document.querySelector(".popup-sign").style.display = "flex";
            })
            document.querySelector(".sign-close").addEventListener("click", function(){
                document.querySelector(".popup-sign").style.display = "none";
            })
