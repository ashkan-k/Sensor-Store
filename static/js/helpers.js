function parseError(e, msg='خطا در دریافت اطلاعات') {
              let statusCode = e.status;
              if (statusCode === 404) {
                  createToast('error', 'صفحه یا مسیر مورد نظر یافت نشد. ممکن‌ است دسترسی لازم را نداشته باشید.');
              } else if (statusCode === 403) {
                  createToast('error', 'شما دسترسی به این آیتم را ندارید.');
              } else {
                  try {
                      let error = e.data['non_field_errors'][0];
                      if (error) {
                          createToast('error', error);
                      }
                  } catch (e) {
                      createToast('error', msg);
                  }
              }
          }
function createToast(type, text) {
            let bgColor = '';
            let header = '';
            if (type === 'error') {
              header = 'خطایی رخ داده';
              bgColor = '#e6294b';
            } else if (type === 'warning') {
              header = 'اخطار';
              bgColor = "#ffb22b";
            } else {
              header = "موفقیت آمیز";
              bgColor = "#06d79c";
            }
            $.toast({
              heading: header,
              text: text,
              position: 'bottom-left',
              bgColor: bgColor,
              loaderBg: "rgb(13, 146, 108)",
              loader: true,
              hideAfter: 3000,
              stack: 3
            });
          }
function createSwal(type, text, title, showCancel = true, confirmText = 'بله،مطمئن‌ام', cancelText = "انصراف") {
    return Swal.fire({
      title: title,
      text: text,
      type: type,
      showCancelButton: showCancel,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: confirmText,
      cancelButtonText: cancelText
    })
}

// AngularJS Configuration
// var app = angular.module("myApp", []);
// app.config(function ($interpolateProvider, $httpProvider) {
//     $interpolateProvider.startSymbol('[[');
//     $interpolateProvider.endSymbol(']]');
//
//     $httpProvider.defaults.xsrfCookieName = 'csrftoken';
//     $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
// });

// app.config(['ADMdtpProvider', function (ADMdtp) {
//         ADMdtp.setOptions({
//           calType: 'jalali',
//           format: 'YYYY-MM-DD',
//         });
//       }]);
// app.filter('riyalBeautifier', function ($filter) {
//         return function (item) {
//           let noCommaStr = item.toString().replace(/,/g, '');
//           noCommaStr += '';
//           x = noCommaStr.split('.');
//           x1 = x[0];
//           x2 = x.length > 1 ? '.' + x[1] : '';
//           var rgx = /(\d+)(\d{3})/;
//           while (rgx.test(x1)) {
//             x1 = x1.replace(rgx, '$1' + ',' + '$2');
//           }
//           return x1 + x2;
//         };
//       });