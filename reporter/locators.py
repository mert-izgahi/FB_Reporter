from selenium.webdriver.common.by import By

class Locator:
    USERNAME_FIELD = (
        By.XPATH,
        "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input",
    )

    PASSWORD_FIELD = (
        By.XPATH,
        "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input",
    )

    LOGIN_BUTTON = (
        By.XPATH,
        "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button",
    )

    OPTIONS_DROPDOWN_BUTTON = (
        By.XPATH,
        "/html/body/div[1]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[2]/div",
    )

    REPORT_BUTTON = (
        By.XPATH,
        "/html/body/div[1]/div/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]",
    )

    REPORT_MODAL = (
        By.XPATH,
        "/html/body/div[1]/div/div/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div",
    )

    REPORT_MODAL_BUTTON = (
        By.XPATH,
        '<div class="x9f619 x1n2onr6 x1ja2u2z x1qjc9v5 x78zum5 xdt5ytf x1iyjqo2 xl56j7k xeuugli x1pi30zi x1swvt13 xsag5q8 xz9dl7a xykv574 xbmpl8g x4cne27 xifccgj xbktkl8"><div class="x9f619 x1ja2u2z x78zum5 x2lah0s x1n2onr6 x1qughib x6s0dn4 xozqiw3 x1q0g3np"><div class="x9f619 x1ja2u2z x78zum5 x1n2onr6 x1iyjqo2 xs83m0k xeuugli x1qughib x6s0dn4 x1a02dak x1q0g3np xdl72j9"><div class="x9f619 x1n2onr6 x1ja2u2z x78zum5 xdt5ytf x2lah0s x193iq5w xeuugli x1iyjqo2"><div class="x9f619 x1n2onr6 x1ja2u2z x78zum5 xdt5ytf x2lah0s x193iq5w xeuugli xsyo7zv x16hj40l x10b6aqq x1yrsyyn"><div class="x78zum5 xdt5ytf xz62fqu x16ldp7u"><div class="xu06os2 x1ok221b"><span class="x193iq5w xeuugli x13faqbe x1vvkbs xlh3980 xvmahel x1n0sxbx x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x3x7a5m x1lkfr7t x1lbecb7 xk50ysn xzsf02u x1yc453h" dir="auto">Bu sayfa hakkında bir şeyler</span></div></div></div></div></div><div class="x9f619 x1n2onr6 x1ja2u2z xdt5ytf x2lah0s x193iq5w xeuugli x78zum5"><div class="x9f619 x1n2onr6 x1ja2u2z x78zum5 xdt5ytf x2lah0s x193iq5w xeuugli xsyo7zv x16hj40l x10b6aqq x1yrsyyn"><svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor" aria-hidden="true" class="xfx01vb x1lliihq x1tzjh5l x1k90msu x2h7rmj x1qfuztq" style="--color: var(--secondary-icon);"><path d="M8.293 3.293a1 1 0 0 1 1.414 0c.887.887 1.778 1.775 2.669 2.663 1.428 1.424 2.859 2.85 4.281 4.28a2.497 2.497 0 0 1-.004 3.526 7797.1 7797.1 0 0 1-4.265 4.266c-.894.893-1.788 1.786-2.68 2.68a1 1 0 0 1-1.415-1.415l2.682-2.68c1.421-1.422 2.843-2.842 4.263-4.264a.497.497 0 0 0 .002-.702c-1.42-1.428-2.845-2.848-4.271-4.27-.892-.888-1.784-1.778-2.676-2.67a1 1 0 0 1 0-1.414z"></path></svg></div></div></div></div>',
    )

    REPORT_TYPE_BUTTON = (
        By.XPATH,
        "/html/body/div[1]/div/div/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div",
    )

    REPORT_SECOND_TYPE_BUTTON = (
        By.XPATH,
        "/html/body/div[1]/div/div/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div[2]/div/div/div/div[7]/div",
    )

    REPORT_THIRD_TYPE_BUTTON = (
        By.XPATH,
        "/html/body/div[1]/div/div/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div[2]/div/div/div/div[1]/div",
    )

    SEND_REPORT_BUTTON = (
        By.XPATH,
        "/html/body/div[1]/div/div/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[5]/div[2]/div/div/div",
    )
