function check() {
    var form = document.forms["contact-form"];
    Array.from(form.elements).forEach(element => {
        if (element.value == '' || element.value == null || element.value == undefined || element.value == ' ') {
            alert("Please Fill All Fields");
            return false;
        };
    });
    return true;
}