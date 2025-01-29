let x = document.getElementsByClassName('submit')
let l = x.length
let form = document.getElementById('details-form')

function validation(i) {

    let inputList = document.getElementsByClassName(`input${i}`)

    for(j = 0; j<inputList.length; j++){

        inputList[j].setCustomValidity('');
        if(!inputList[j].checkValidity()){
            inputList[j].reportValidity();
            return false
        }

        if(i == 1){

            if(inputList[j].name == "gender"){
                if(!["male","female"].includes(String(inputList[j].value).trim().toLowerCase())){
                    inputList[j].setCustomValidity(`Enter either "Male" or "Female"`)
                    inputList[j].reportValidity()
                    return false
                }
            }

        }

    }

}

for(i = 0; i<l; i++){
    x[i].onclick = ((num, form) => {
        return () => {
            
            let gender = document.getElementById('gender').value
            
            if(num < l-1){
                document.getElementsByClassName('form-container')[num].classList.add('no-display')
                if(num == 2 && gender.toLowerCase() == "male"){
                    num += 1
                }else if(num == 2 && gender.toLowerCase() == "female"){
                    let female_num_inputs = document.querySelectorAll('#form-container4 input[type=number]');
                    female_num_inputs.forEach(input=> {
                        input.required = true;
                    })
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