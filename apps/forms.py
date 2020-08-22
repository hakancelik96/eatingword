from django import forms


class SemanticFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            widget = self.fields[field_name].widget
            while hasattr(widget, "widget"):
                widget = widget.widget
            if "nosemantic" in widget.attrs:
                continue
            class_names = [widget.attrs.get("class", "")]
            if isinstance(widget, forms.widgets.DateTimeBaseInput):
                class_names.extend(["datetimepicker", "form-control"])
            elif isinstance(widget, forms.Select):
                # widget.attrs["data-live-search"] = "true"
                widget.attrs["title"] = (
                    "Select " + field_name.replace("_", " ").title()
                )
                # widget.attrs["data-selected-text-format"] = "count > 2"
                # widget.attrs["data-size"] = "5"
                # widget.attrs["data-actions-box"] = "true"
                class_names.extend(
                    [
                        # "selectpicker",
                        # "show-menu-arrow",
                        "ui",
                        "dropdown",
                        "search",
                    ]
                )
            elif isinstance(widget, forms.FileInput):
                class_names.extend(["form-control-file"])
            elif isinstance(widget, forms.Textarea):
                class_names.extend(["summernote", "form-control"])
            else:
                class_names.extend(["form-control"])
            widget.attrs["class"] = " ".join(class_names)
            widget.attrs.setdefault("autocomplete", "off")
            widget.attrs.setdefault(
                "placeholder", field_name.replace("_", " ").title()
            )
