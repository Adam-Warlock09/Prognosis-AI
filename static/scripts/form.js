let x = document.getElementsByClassName('submit')
let l = x.length
let form = document.getElementById('details-form')

for(i = 0; i<l; i++){
    x[i].onclick = ((num, form) => {
        return () => {
            
            let gender = document.getElementById('gender').value
            
            if(num < l-1){
                document.getElementsByClassName('form-container')[num].classList.add('no-display')
                if(num == 2 && gender.toLowerCase() == "male"){
                        num += 1
                    }
                    document.getElementsByClassName('form-container')[num + 1].classList.remove('display')
                }else{
                    console.log("hello")
                    // form.submit()
                    console.log("hello submitted")
                }

        }
    })(i,form)
}