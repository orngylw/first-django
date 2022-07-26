

def process_modal_vars(title, content, label, url=None):
    return {
        "modal_title": title,
        "modal_content": content,
        "modal_submit_label": label,
        "form_action": url,
    }

