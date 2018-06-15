// lazyload config
var MODULE_CONFIG = {
    chat:           [
                      '/static/common/libs/list.js/dist/list.js',
                      '/static/common/libs/notie/dist/notie.min.js',
                      '/static/common/js/plugins/notie.js',
                      '/static/common/js/app/chat.js'
                    ],
    mail:           [
                      '/static/common/libs/list.js/dist/list.js',
                      '/static/common/libs/notie/dist/notie.min.js',
                      '/static/common/js/plugins/notie.js',
                      '/static/common/js/app/mail.js'
                    ],
    user:           [
                      '/static/common/libs/list.js/dist/list.js',
                      '/static/common/libs/notie/dist/notie.min.js',
                      '/static/common/js/plugins/notie.js',
                      '/static/common/js/app/user.js'
                    ],
    screenfull:     [
                      '/static/common/libs/screenfull/dist/screenfull.js',
                      '/static/common/js/plugins/screenfull.js'
                    ],
    jscroll:        [
                      '/static/common/libs/jscroll/jquery.jscroll.min.js'
                    ],
    stick_in_parent:[
                      '/static/common/libs/sticky-kit/jquery.sticky-kit.min.js'
                    ],
    scrollreveal:   [
                      '/static/common/libs/scrollreveal/dist/scrollreveal.min.js',
                      '/static/common/js/plugins/jquery.scrollreveal.js'
                    ],
    owlCarousel:    [
                      '/static/common/libs/owl.carousel/dist/assets/owl.carousel.min.css',
                      '/static/common/libs/owl.carousel/dist/assets/owl.theme.css',
                      '/static/common/libs/owl.carousel/dist/owl.carousel.min.js'
                    ],
    html5sortable:  [
                      '/static/common/libs/html5sortable/dist/html.sortable.min.js',
                      '/static/common/js/plugins/jquery.html5sortable.js',
                      '/static/common/js/plugins/sortable.js'
                    ],
    easyPieChart:   [
                      '/static/common/libs/easy-pie-chart/dist/jquery.easypiechart.min.js'
                    ],
    peity:          [
                      '/static/common/libs/peity/jquery.peity.js',
                      '/static/common/js/plugins/jquery.peity.tooltip.js',
                    ],
    chart:          [
                      '/static/common/libs/moment/min/moment-with-locales.min.js',
                      '/static/common/libs/chart.js/dist/Chart.min.js',
                      '/static/common/js/plugins/jquery.chart.js',
                      '/static/common/js/plugins/chartjs.js'
                    ],
    dataTable:      [
                      '/static/common/libs/datatables/media/js/jquery.dataTables.min.js',
                      '/static/common/libs/datatables.net-bs4/js/dataTables.bootstrap4.js',
                      '/static/common/libs/datatables.net-bs4/css/dataTables.bootstrap4.css',
                      '/static/common/js/plugins/datatable.js'
                    ],
    bootstrapTable: [
                      '/static/common/libs/bootstrap-table/dist/bootstrap-table.min.css',
                      '/static/common/libs/bootstrap-table/dist/bootstrap-table.min.js',
                      '/static/common/libs/bootstrap-table/dist/extensions/export/bootstrap-table-export.min.js',
                      '/static/common/libs/bootstrap-table/dist/extensions/mobile/bootstrap-table-mobile.min.js',
                      '/static/common/js/plugins/tableExport.min.js',
                      '/static/common/js/plugins/bootstrap-table.js'
                    ],
    bootstrapWizard:[
                      '/static/common/libs/twitter-bootstrap-wizard/jquery.bootstrap.wizard.min.js'
                    ],
    dropzone:       [
                      '/static/common/libs/dropzone/dist/min/dropzone.min.js',
                      '/static/common/libs/dropzone/dist/min/dropzone.min.css'
                    ],
    datetimepicker: [
                      '/static/common/libs/tempusdominus-bootstrap-4/build/css/tempusdominus-bootstrap-4.min.css',
                      '/static/common/libs/moment/min/moment-with-locales.min.js',
                      '/static/common/libs/tempusdominus-bootstrap-4/build/js/tempusdominus-bootstrap-4.min.js',
                      '/static/common/js/plugins/datetimepicker.js'
                    ],
    datepicker:     [
                      "/static/common/libs/bootstrap-datepicker/dist/js/bootstrap-datepicker.min.js",
                      "/static/common/libs/bootstrap-datepicker/dist/css/bootstrap-datepicker.min.css",
                    ],
    fullCalendar:   [
                      '/static/common/libs/moment/min/moment-with-locales.min.js',
                      '/static/common/libs/fullcalendar/dist/fullcalendar.min.js',
                      '/static/common/libs/fullcalendar/dist/fullcalendar.min.css',
                      '/static/common/js/plugins/fullcalendar.js'
                    ],
    parsley:        [
                      '/static/common/libs/parsleyjs/dist/parsley.min.js'
                    ],
    select2:        [
                      '/static/common/libs/select2/dist/css/select2.min.css',
                      '/static/common/libs/select2/dist/js/select2.min.js',
                      '/static/common/js/plugins/select2.js'
                    ],
    summernote:     [
                      '/static/common/libs/summernote/dist/summernote.css',
                      '/static/common/libs/summernote/dist/summernote-bs4.css',
                      '/static/common/libs/summernote/dist/summernote.min.js',
                      '/static/common/libs/summernote/dist/summernote-bs4.min.js'
                    ],
    vectorMap:      [
                      '/static/common/libs/jqvmap/dist/jqvmap.min.css',
                      '/static/common/libs/jqvmap/dist/jquery.vmap.js',
                      '/static/common/libs/jqvmap/dist/maps/jquery.vmap.world.js',
                      '/static/common/libs/jqvmap/dist/maps/jquery.vmap.usa.js',
                      '/static/common/libs/jqvmap/dist/maps/jquery.vmap.france.js',
                      '/static/common/js/plugins/jqvmap.js'
                    ],
    waves:          [
                      '/static/common/libs/node-waves/dist/waves.min.css',
                      '/static/common/libs/node-waves/dist/waves.min.js',
                      '/static/common/js/plugins/waves.js'
                    ]
  };

var MODULE_OPTION_CONFIG = {
  parsley: {
    errorClass: 'is-invalid',
    successClass: 'is-valid',
    errorsWrapper: '<ul class="list-unstyled text-sm mt-1 text-muted"></ul>'
  }
}
