import random
import string

home = "https://lamp-frontend.herokuapp.com"
login_page_button = "//div[@id='app']/div/div[2]/div/header/div/div/div[@class='justify-lg-space-between']/div/button[1]"

# =========================================
# Login page locators                     #
# =========================================
login_button = "//div[@id='app']//main[@class='v-main']/div/div/div/div[1]/div//form//button[@type='submit']/span[@class='v-btn__content']"
email_field = '//input[@type="text"]'
password_field = '//input[@placeholder="Password" and @type="password"]'
email = 'tboydv1@gmail.com'
password = '123pass321'

# =========================================
# Dashboard                             #
# =========================================
dashbaord_tab = "//div[@id='app']//nav/div[@class='v-navigation-drawer__content']/div/div/div[@role='tablist']//div[@class='v-slide-group__content v-tabs-bar__content']/a[1]/span[.='Dashboard']"
snackbar_alert = "//div[@id='app']//div[@role='alert']"
# =========================================
# Trainees page                   #
# =========================================
trainees_tab = '//*[@id="app"]/div/div[2]/div/nav/div[1]/div/div/div/div[2]/div/a[2]/span'
trainees_page_heading = "//div[@id='app']//main[@class='v-main']/div/div/div/div[1]/div/h2[@class='ma-3']"
trainee_page_header_text = 'Trainees'
invite_button = "/html//div[@id='app']//main[@class='v-main']/div/div/div/div[2]/div/div/div/div[1]/div[4]/div/button[@role='button']/span/button[@type='button']"
trainee_checkbox = '//*[@id="app"]/div[1]/main/div/div/div/div[2]/div/div/div/div[3]/div/table/tbody/tr[2]/td[1]/div/i'
trainee_record = "/html//div[@id='app']//main[@class='v-main']/div/div/div/div[2]/div/div/div/div[3]/div[@class='v-data-table__wrapper']/table/tbody/tr[1]"
trainee_selection_checkbox = "/html//div[@id='app']/div[@class='v-application--wrap']/main[@class='v-main']/div[@class='v-main__wrap']/div/div/div[2]/div/div/div/div[3]/div[@class='v-data-table__wrapper']/table/tbody/tr[1]/td[1]/div[@class='v-data-table__checkbox v-simple-checkbox']/i"
# ======== Search =========
search_field = "/html//div[@id='app']//main[@class='v-main']/div/div/div/div[2]/div/div/div/div[1]/div[1]/div//div[@class='v-input__slot']//input[@type='text']"
search_email = 'tboydv1@gmail.com'
search_result = "//div[@id='app']/div[@class='v-application--wrap']/main[@class='v-main']/div/div/div/div[2]/div/div/div/div[3]/div[@class='v-data-table__wrapper']/table/tbody"
search_result_name = 'Chinonso okoroafor'
search_result_role = 'HR'

# =========  Invite modal ==========
invite_modal_heading = "//div[@id='app']/div[@role='document']/div/div//h2[.='Invite Trainees']"
invite_modal_heading_text = 'Invite Trainees'
send_invite_button = "//div[@id='app']/div[3]/div/div/div/div[@class='row']/div[2]/div/div[3]/button[2]"
invite_email_field = "/html//div[@id='app']/div[@role='document']/div/div/div/div/div[2]/div//input[@type='text']"
invite_add_button = "//div[@id='app']/div[@role='document']/div/div/div/div[@class='row']/div[2]/div/div[1]/div[2]/button[@type='button']"
invite_modal_search = "//div[@id='app']/div[@role='document']/div/div/div/div[@class='row']/div[2]/div//input[@type='text']"
invite_email = 'test@yupmail.com'
email_added = "//div[@id='dropdown']/div[@class='v-data-table__wrapper']/table/tbody/tr/td[1]"
invite_success_modal = "//div[@id='app']/div[4]/div/div//h3[.='Invites Sent!']"
invite_success_message = "Invites Sent!"
invite_close_button = "//div[@id='app']/div[4]//button[@type='button']"

# ======Assign Course Modal=======
assign_course_modal = "//div[@id='app']/div[@role='document']/div/div//div[@class='v-card__title']"
assign_course_icon = "//div[@id='app']/div[@class='v-application--wrap']/main[@class='v-main']/div/div/div/div[2]/div/div/div/div[2]/div[3]/div[2]/button[@role='button']//i"
assign_course_dropdown = "//div[@id='app']/div[@role='document']/div/div/div//div[@role='button']//i"
assign_course_select = "//div[@id='app']//div[@role='listbox']/div[1]"
assign_course_button = "//div[@id='app']/div[@role='document']/div/div/div/div/div[5]/button[2]"

# ======Groups page=======
groups_tab_button = "//div[@id='app']//main[@class='v-main']/div/div/div/div[1]/div/div/div[@role='tablist']//div[@class='v-slide-group__content v-tabs-bar__content']/a[2]"
create_group_button = "/html//div[@id='app']//main[@class='v-main']/div/div/div/div[2]/div/div[1]/div[3]/button[@role='button']"
create_group_modal = "//div[@id='app']/div[@role='document']//div[.='Create a Group']"
group_dropdown = "//div[@id='app']/div[@role='document']/div/div/div[@class='mx-16']/div[1]/div[@class='v-input__control']/div[@role='button']//i"
select_other_groups = "//div[@id='app']//div[@role='listbox']/div[1]/div[@class='v-list-item__content']"
group_name_field = "//div[@id='app']/div[@role='document']/div/div/div[@class='mx-16']/div[2]/div[@class='v-input__control']/div[@class='v-input__slot']"
group_name = 'QA' + ''.join(random.choices(string.ascii_uppercase +
                                           string.digits, k=7))
