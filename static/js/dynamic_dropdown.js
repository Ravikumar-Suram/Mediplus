// document.addEventListener("DOMContentLoaded", function () {
//   var departmentSelect = document.querySelector('select[name="department"]');
//   var doctorSelect = document.querySelector('select[name="doctor"]');
//   var specialtySelect = document.querySelector('select[name="specialty"]');

//   // Function to update doctors based on selected specialty
//   function updateDoctors() {
//     var specialty = specialtySelect.value;
//     doctorSelect.innerHTML = ""; // Clear existing options

//     if (specialty) {
//       fetch(`/get_doctors/?specialty=${specialty}`)
//         .then((response) => response.json())
//         .then((data) => {
//           data.forEach((doctor) => {
//             var option = document.createElement("option");
//             option.textContent = doctor.name;
//             option.value = doctor.id;
//             doctorSelect.appendChild(option);
//           });
//         })
//         .catch((error) => console.error("Error fetching doctors:", error));
//     }
//   }

//   // Event listener to trigger updateDoctors function when specialty selection changes
//   specialtySelect.addEventListener("change", updateDoctors);

//   // Function to update specialties based on selected department
//   function updateSpecialties() {
//     var department = departmentSelect.value;
//     specialtySelect.innerHTML = ""; // Clear existing options

//     if (department) {
//       fetch(`/get_specialties/?department=${department}`)
//         .then((response) => response.json())
//         .then((data) => {
//           data.forEach((specialty) => {
//             var option = document.createElement("option");
//             option.textContent = specialty;
//             option.value = specialty;
//             specialtySelect.appendChild(option);
//           });
//         })
//         .catch((error) => console.error("Error fetching specialties:", error));
//     }
//   }

//   // Event listener to trigger updateSpecialties function when department selection changes
//   departmentSelect.addEventListener("change", updateSpecialties);

//   // Initial call to update specialties based on default selected department
//   updateSpecialties();

//   // Initial call to update doctors based on default selected specialty
//   updateDoctors();
// });

$(document).ready(function () {
  $("#department-select").change(function () {
    var department = $(this).val();
    if (department) {
      $("#doctor-select").prop("disabled", false);
      $("#doctor-select")
        .empty()
        .append('<option value="" selected disabled>Loading...</option>');
      $.ajax({
        url: "/doctors/",
        type: "GET",
        data: { department_id: department },
        success: function (data) {
          $("#doctor-select")
            .empty()
            .append('<option value="" selected disabled>Doctor</option>');
          $.each(data.doctors, function (index, doctor) {
            $("#doctor-select").append(
              '<option value="' +
                doctor.id +
                '">Dr. ' +
                doctor.name +
                "</option>"
            );
          });
        },
      });
    } else {
      $("#doctor-select").prop("disabled", true);
      $("#doctor-select")
        .empty()
        .append('<option value="" selected disabled>Doctor</option>');
    }
  });
});
