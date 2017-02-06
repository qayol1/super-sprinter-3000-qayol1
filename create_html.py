from story import Story


class Create_html:
    @staticmethod
    def print_separator_line(f, number_of_clomns):
        f.write("<tr>\n")
        for i in range((number_of_clomns * 2) + 1):
            if i % 2 == 1:
                f.write("<th>-------------</th>\n")
            else:
                f.write("<th>-</th>\n")
        f.write("</tr>\n")

    @staticmethod
    def create_list_html():
        with open('/home/peter/python/first_flask_homework/templates/list.html', 'w') as f:
            f.write("<!DOCTYPE html>\n")
            f.write("<html lang='en'>\n")
            f.write("<head>\n")
            f.write("<meta charset='UTF-8'>\n")
            f.write("<title>Super Sprinter 3000</title>\n")
            f.write("</head>\n")
            f.write("<body>\n")
            f.write("<h2>Super Sprinter 3000</h2>\n")
            f.write("<form action='story'>\n")
            f.write("<input type='submit' value='Add a new user story' />\n")
            f.write("</form>\n")
            f.write("<p>\n")
            f.write("<table>\n")
            column_name = ["ID", "Story", "User Story", "Acceptance Criteria", "Business Value", "Estimation", "Status"]
            Create_html.print_separator_line(f, len(column_name))
            f.write("<tr>\n")
            f.write("<th>|</th>\n")
            for element in column_name:
                f.write("<th>" + element + "</th>\n")
                f.write("<th>|</th>\n")
            f.write("</tr>\n")
            Create_html.print_separator_line(f, len(column_name))
            story = Story.select()
            for element in story:
                f.write("<tr>\n")
                column_element = [str(element.id), element.title, element.description, element.acceptance_criteria,
                                  str(element.business_value), str(element.estimation_hour), element.status]
                f.write("<th>|</th>\n")
                for element in column_element:
                    f.write("<th>" + element + "</th>\n")
                    f.write("<th>|</th>\n")
                f.write("<th><a href='story/" + str(
                    column_element[0]) + "'><img src='quill.gif' alt='pen' height='15' width='15'/></a></th>\n")
                f.write("<th><a href='delete/" + str(
                    column_element[0]) + "'><img src='bin.jpg' alt='bin' height='15' width='15'/></a></th>\n")
                f.write("</tr>\n")
            Create_html.print_separator_line(f, len(column_name))
            f.write("</table>\n")
            f.write("</p>\n")
            f.write("</body>\n")
            f.write("</html>\n")

    @staticmethod
    def create_form_html(id=None):
        if id:
            story = Story.get(Story.id == id)
        else:
            story = Story()
            story.title = ""
            story.description = ""
            story.acceptance_criteria = ""
        with open('/home/peter/python/first_flask_homework/templates/form.html', 'w') as f:
            f.write("<!DOCTYPE html>\n")
            f.write("<html lang='en'>\n")
            f.write("<head>\n")
            f.write("<meta charset='UTF-8'>\n")
            f.write("<title> Super Sprinter 3000 </title>\n")
            f.write("</head>\n")
            f.write("<body>\n")
            if id:
                f.write("<h2> Super Sprinter 3000 - Edit Story </h2>\n")
            else:
                f.write("<h2> Super Sprinter 3000 - Add new Story </h2>\n")
            if id:
                f.write("<form action = 'update_story/" + str(story.id) + "' method='post'>\n")
            else:
                f.write("<form action='save_story' method = 'post'>\n")
            f.write("<p><label for='story_title'>Story Title</label><br></p>\n")
            f.write(
                "<input type='text' name='story_title' id='story_title' value='" + story.title + "' size='81' required>\n")
            f.write("<p><label for='user_story'>User Story</label><br></p>\n")
            f.write(
                "<textarea name='user_story' id='user_story' rows='5' cols='80' required>" + story.description + "</textarea>\n")
            f.write("<p><label for='acceptance_criteria'>Acceptance Criteria</label><br></p>\n")
            f.write(
                "<textarea name='acceptance_criteria' id='acceptance_criteria' rows='5' cols='80' required>" + story.acceptance_criteria + "</textarea>\n")
            f.write("<p><label for='business_value'>Business Value</label><br></p>\n")
            if id:
                f.write(
                    "<input type='number' name='business_value' id='business_value' step='100' min='100' max='1500' value=" + str(
                        story.business_value) + " required>\n")
            else:
                f.write(
                    "<input type='number' name='business_value' id='business_value' step='100' min='100' max='1500' value=100 required>\n")
            f.write("<p><label for='estimation_hour'>Estimation Hour</label><br></p>\n")
            if id:
                f.write(
                    "<input type='number' name='estimation_hour' id='estimation_hour' step='0.5' min='0.5' max='40' value=" + str(
                        story.estimation_hour) + " required>\n")
            else:
                f.write(
                    "<input type='number' name='estimation_hour' id='estimation_hour' step='0.5' min='0.5' max='40' value='0.5' required>\n")
            f.write("<p><label for='status'>Status</label><br></p>\n")
            f.write("<select name='status' id='status' required>\n")
            if id:
                if story.status == "Planning":
                    f.write("<option selected> Planning </option>\n")
                else:
                    f.write("<option> Planning </option>\n")

                if story.status == "To Do":
                    f.write("<option selected> To Do </option>\n")
                else:
                    f.write("<option> To Do </option>\n")

                if story.status == "In progress":
                    f.write("<option selected> In progress </option>\n")
                else:
                    f.write("<option> In progress </option>\n")

                if story.status == "Review":
                    f.write("<option selected> Review </option>\n")
                else:
                    f.write("<option> Review </option>\n")

                if story.status == "Done":
                    f.write("<option selected> Done </option>\n")
                else:
                    f.write("<option> Done </option>\n")
            else:
                f.write("<option> Planning </option>\n")
                f.write("<option> To Do </option>\n")
                f.write("<option> In progress </option>\n")
                f.write("<option> Review </option>\n")
                f.write("<option> Done </option>\n")
            f.write("</select>\n")
            f.write("<p>\n")
            if id:
                f.write("<input type = 'submit' value='Update story'>\n")
            else:
                f.write("<input type='submit' value='Save story'>\n")
            f.write("</p>\n")
            f.write("</form>\n")
            f.write("</body>\n")
            f.write("</html>\n")
