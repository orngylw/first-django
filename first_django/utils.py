

def process_modal_vars(title, content, label, url=None):
    return {
        "modal_title": title,
        "modal_content": content,
        "modal_submit_label": label,
        "form_action": url,
    }


def process_form_vars(label, back_url=None, action_url="."):
    return {
        "form_submit_label": label,
        "form_reverse": back_url,
        "form_action": action_url,
    }