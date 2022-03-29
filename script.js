function validate() {
    let name = document.forms["form"]["name"].value;
    let email = document.forms["form"]["email"].value;
    let phone = document.forms["form"]["phone"].value;
    let areacode = document.forms["form"]["areacode"].value;
    let comment = document.forms["form"]["comment"].value;

    if(validator(name, email, phone, areacode, comment)) {
        return true;
    }
    else{return false;}
}

/*
Checks every field for invalid input
*/
function validator(name, email, phone, areacode, comment) {
    for (var i = 0, j = arguments.length; i < j; i++){ // Make sure no field has a semicolon
        if (containsSemicolon(arguments[i])) {
            printErrorMsg("Felten kan ikke inneholde semikolon.");
            return false;}
    }

    if (!(emailValidator(email))) {
        printErrorMsg("Ikke gyldig Email adresse.");
        return false;
    }

    if (!(phoneValidator(phone))) {
        printErrorMsg("Ikke gyldig telefon nummer.");
        return false;
    }

    if (!(areacodeValidator(areacode))) {
        printErrorMsg("Ikke gyldig postnummer.");
        return false;
    }

    return true;

}

/*
True if str contains semicolon, 
Semicolon is reserved for the divider in the python script (verifyData.py)
*/
function containsSemicolon(str) {
    return str.includes(";");
}

/*
True if email is valid
*/
function emailValidator(str) {
    const nameAndDomain = str.split("@");
    if (nameAndDomain.length == 2){ // Make sure email has name and domain, and only a single @
        if (nameAndDomain[1].includes(".")){return true;} // Make sure domain contains "."
    }
    return false;
}

/*
True if phone number is valid
*/
function phoneValidator(str) {
    let legalStartingDigits = ["2","4","5","6","8","9"] // Norwegian private numbers start with these digits
    if (/^\d+$/.test(str)){ // Regex expression to check if input consist of numbers
        if (str.length == 8){ // Phone number must be 8 digits long
            if (legalStartingDigits.includes(str.charAt(0))){ // Make sure the first digit is valid
                return true;
            }
        }
    }
    return false;
}

/*
True if areacode is valid
*/
function areacodeValidator(str) {
    if (/^\d+$/.test(str)){ // Regex expression to check if input consist of numbers
        if (str.length == 4){
            return true;
        }
    }
        return false;
}

function printErrorMsg(str) {
    document.getElementById("errorMessage").innerHTML = str;
}