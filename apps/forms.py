from django import forms


class UikitFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            widget = self.fields[field_name].widget
            while hasattr(widget, "widget"):
                widget = widget.widget
            if "nouikit" in widget.attrs:
                continue
            class_names = [widget.attrs.get("class", "")]
            # if isinstance(widget, forms.widgets.DateTimeBaseInput):
            #     class_names.extend(["datetimepicker", "form-control"])
            if isinstance(widget, forms.Select):
                widget.attrs["title"] = (
                    "Select " + field_name.replace("_", " ").title()
                )
                class_names.extend(["uk-select"])
            elif isinstance(widget, forms.Textarea):
                class_names.extend(["uk-textarea"])
            class_names.extend(["uk-input", "uk-form-width-large"])
            widget.attrs["class"] = " ".join(class_names)
            widget.attrs.setdefault("autocomplete", "off")
            widget.attrs.setdefault(
                "placeholder", field_name.replace("_", " ").title()
            )
            uk_icons = {
                "username": "user",
                "password": "lock",
                "password1": "lock",
                "password2": "lock",
            }
            widget.uk_icon = uk_icons.get(field_name, None)
            widget.label_classes = ("uk-form-label",)
