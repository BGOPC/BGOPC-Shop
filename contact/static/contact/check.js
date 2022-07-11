function check() {
    var form = document.forms["contact-form"];
    Array.from(form.elements).forEach(element => {
        if (element.value == '' || element.value == null || element.value == undefined || element.value == ' ') return false;
    });
    return true;
}