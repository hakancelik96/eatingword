document.addEventListener(
  "DOMContentLoaded",
  function () {
    /* toasatr */
    toastr.options = {
      closeButton: true,
      debug: false,
      newestOnTop: true,
      progressBar: true,
      positionClass: "toast-bottom-right",
      preventDuplicates: false,
      onclick: null,
      showDuration: "300",
      hideDuration: "1000",
      timeOut: "5000",
      extendedTimeOut: "1000",
      showEasing: "swing",
      hideEasing: "linear",
      showMethod: "fadeIn",
      hideMethod: "fadeOut",
    };
    let messages = document.head.querySelectorAll("meta[name=message]");
    for (let message of messages) {
      let tagName = message.dataset["tag"];
      let content = message.content;
      eval(`toastr.${tagName}`)(content);
    }
    /* forms validation check */
    document
      .querySelector("button[type=submit]")
      .addEventListener("click", function () {
        let form = this.form;
        let formIsValid = form.checkValidity();
        if (formIsValid) {
          this.innerText = "Loading ... ";
          this.setAttribute("uk-spinner", "");
          this.setAttribute("disabled", "");
          form.submit();
        } else {
          form.setAttribute("class", "shake-horizontal");
          setTimeout(function () {
            form.removeAttribute("class", "shake-horizontal");
          }, 400);
          toastr.warning("Form is not valid");
          this.removeAttribute("disabled");
        }
      });
  },
  false
);
