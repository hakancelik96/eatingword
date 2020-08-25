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
        if (form.checkValidity()) {
          this.setAttribute("disabled", "");
          this.innerText = "Loading ... ";
          this.setAttribute("uk-spinner", "");
          form.submit();
        } else {
          this.toggleAttribute("disabled");
          let currentClasses = form.getAttribute("class");
          form.setAttribute("class", `${currentClasses} uk-animation-shake`);
          setTimeout(function () {
            form.setAttribute("class", currentClasses);
          }, 400);
          toastr.warning("Form Is Not Valid");
          this.removeAttribute("disabled");
        }
      });
  },
  false
);
