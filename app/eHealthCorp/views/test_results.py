from flask import Blueprint, render_template, request, send_file
from io import BytesIO
from eHealthCorp import get_conn


test_results = Blueprint("/test_results", __name__, template_folder="templates")

@test_results.route("/test_results", methods=["GET", "POST"])
def show():

    if request.method == 'POST':
        test_code = request.form["code"].strip()
        
        #test code pre-evalution
        if test_code[:3] != "EHC":
            return render_template("test_results.html", error=True)
        elif not test_code[3:].isnumeric() != "EHC":
            return render_template("test_results.html", error=True)

        test_code = test_code[3:]

        try:
            conn, cur = get_conn()
            test_result = cur.execute("SELECT file_name_, file_data FROM test_results WHERE id = ?", (test_code)).fetchone()
            conn.close()


            if test_result is None:
                return render_template("test_results.html", error=True)
            return send_file(BytesIO(test_result[1]), download_name=test_result[0], as_attachment=True)

        except:
            return render_template("error.html", error="Error while getting test result file.")

    return render_template("test_results.html")