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
    $("button[type=submit]").click(function () {
      let form = this.form;
      console.log(form);
      let formIsValid = form.checkValidity();
      if (formIsValid) {
        this.setAttribute("disabled", "");
        this.innerHTML = "";
        $(this).prepend(
          `<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Loading...`
        );
        form.submit();
      } else {
        $(form).addClass("shake-horizontal");
        setTimeout(function () {
          $(form).removeClass("shake-horizontal");
        }, 400);
        toastr.warning("Form is not valid");
        this.removeAttribute("disabled");
      }
    });
  },
  false
);
