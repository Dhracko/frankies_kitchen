$(document).ready(function () {
  /*
    Funtions to count the characters left on the input for recipe name and 
    the short description. It will calculate the remaining characters and 
    tell the user the number.
    */
  $("#recipe_name").keypress(function () {
    if (this.value.length > 30) {
      return false;
    }
    $("#recipe-name-count").html(
      "Remaining characters : " + (30 - this.value.length)
    );
  });

  $("textarea").keypress(function () {
    if (this.value.length > 120) {
      return false;
    }
    $("#description-count").html(
      "Remaining characters : " + (120 - this.value.length)
    );
  });

  /* Functions to add an extra line to the Ingredients and to the Method Steps. */
  $("#add_ingredient").on("click", () => {
    $("#remove_ingredient").removeAttr("disabled", "disabled");
    $("#ingredient").append(
      '<input class="form-control my-2" type="text" name="ingredients" pattern="^[a-zA-Z0-9]+( [a-zA-Z0-9.z()-,]+)*$" title="Must start with an uppercase or lowercase word. Acceptable characters are hyphens, commas, periods, and brackets. Cannot start with a space." required>'
    );
  });

  $("#add_step").on("click", () => {
    $("#remove_step").removeAttr("disabled", "disabled");
    $("#step_inputs").append(
      '<input class="form-control my-2" type="text" name="step" pattern="^[a-zA-Z0-9]+( [a-zA-Z0-9.z()-,]+)*$" title="Must start with an uppercase or lowercase word. Acceptable characters are hyphens, commas, periods, and brackets. Cannot start with a space." required>'
    );
  });

  /* Functions to the buttons to remove ingredients and methods steps in the addrecipe.html */
  $("#remove_ingredient").on("click", () => {
    let ingredientLength = $("#ingredient").children("input").length;

    if (ingredientLength <= 1) {
      $("#remove_ingredient").attr("disabled", "disabled");
    } else {
      $("#ingredient input:last-child").remove();
    }
  });

  $("#remove_step").on("click", () => {
    let stepLength = $("#step_inputs").children("input").length;

    if (stepLength <= 1) {
      $("#remove_step").attr("disabled", "disabled");
    } else {
      $("#step_inputs input:last-child").remove();
    }
  });
});


