// lazyload config
var MODULE_CONFIG = {
    chat:           [
                      '../libs/list.js/dist/list.js',
                      '../libs/notie/dist/notie.min.js',
                      'plugins/notie.js',
                      'app/chat.js'
                    ],
    mail:           [
                      '../libs/list.js/dist/list.js',
                      '../libs/notie/dist/notie.min.js',
                      'plugins/notie.js',
                      'app/mail.js'
                    ],
    user:           [
                      '../libs/list.js/dist/list.js',
                      '../libs/notie/dist/notie.min.js',
                      'plugins/notie.js',
                      'app/user.js'
                    ],
    screenfull:     [

                    ],
    jscroll:        [
                      '../libs/jscroll/jquery.jscroll.min.js'
                    ],
    stick_in_parent:[
                      '../libs/sticky-kit/jquery.sticky-kit.min.js'
                    ],
    scrollreveal:   [
                      '../libs/scrollreveal/dist/scrollreveal.min.js',
                      'plugins/jquery.scrollreveal.js'
                    ],
    owlCarousel:    [
                      '../libs/owl.carousel/dist/assets/owl.carousel.min.css',
                      '../libs/owl.carousel/dist/assets/owl.theme.css',
                      '../libs/owl.carousel/dist/owl.carousel.min.js'
                    ],
    html5sortable:  [
                      '../libs/html5sortable/dist/html.sortable.min.js',
                      'plugins/jquery.html5sortable.js',
                      'plugins/sortable.js'
                    ],
    easyPieChart:   [
                      '../libs/easy-pie-chart/dist/jquery.easypiechart.min.js'
                    ],
    peity:          [
                      '../libs/peity/jquery.peity.js',
                      'plugins/jquery.peity.tooltip.js',
                    ],
    chart:          [

                    ],
    dataTable:      [
                      '../libs/datatables/media/js/jquery.dataTables.min.js',
                      '../libs/datatables.net-bs4/js/dataTables.bootstrap4.js',
                      '../libs/datatables.net-bs4/css/dataTables.bootstrap4.css',
                      'plugins/datatable.js'
                    ],
    bootstrapTable: [
                      '../libs/bootstrap-table/dist/bootstrap-table.min.css',
                      '../libs/bootstrap-table/dist/bootstrap-table.min.js',
                      '../libs/bootstrap-table/dist/extensions/export/bootstrap-table-export.min.js',
                      '../libs/bootstrap-table/dist/extensions/mobile/bootstrap-table-mobile.min.js',
                      'plugins/tableExport.min.js',
                      'plugins/bootstrap-table.js'
                    ],
    bootstrapWizard:[
                      '../libs/twitter-bootstrap-wizard/jquery.bootstrap.wizard.min.js'
                    ],
    dropzone:       [
                      '../libs/dropzone/dist/min/dropzone.min.js',
                      '../libs/dropzone/dist/min/dropzone.min.css'
                    ],
    datetimepicker: [
                      '../libs/tempusdominus-bootstrap-4/build/css/tempusdominus-bootstrap-4.min.css',
                      '../libs/moment/min/moment-with-locales.min.js',
                      '../libs/tempusdominus-bootstrap-4/build/js/tempusdominus-bootstrap-4.min.js',
                      'plugins/datetimepicker.js'
                    ],
    datepicker:     [
                      "../libs/bootstrap-datepicker/dist/js/bootstrap-datepicker.min.js",
                      "../libs/bootstrap-datepicker/dist/css/bootstrap-datepicker.min.css",
                    ],
    fullCalendar:   [
                      '../libs/moment/min/moment-with-locales.min.js',
                      '../libs/fullcalendar/dist/fullcalendar.min.js',
                      '../libs/fullcalendar/dist/fullcalendar.min.css',
                      'plugins/fullcalendar.js'
                    ],
    parsley:        [
                      '../libs/parsleyjs/dist/parsley.min.js'
                    ],
    select2:        [
                      '../libs/select2/dist/css/select2.min.css',
                      '../libs/select2/dist/js/select2.min.js',
                      'plugins/select2.js'
                    ],
    summernote:     [
                      '../libs/summernote/dist/summernote.css',
                      '../libs/summernote/dist/summernote-bs4.css',
                      '../libs/summernote/dist/summernote.min.js',
                      '../libs/summernote/dist/summernote-bs4.min.js'
                    ],
    vectorMap:      [
                      '../libs/jqvmap/dist/jqvmap.min.css',
                      '../libs/jqvmap/dist/jquery.vmap.js',
                      '../libs/jqvmap/dist/maps/jquery.vmap.world.js',
                      '../libs/jqvmap/dist/maps/jquery.vmap.usa.js',
                      '../libs/jqvmap/dist/maps/jquery.vmap.france.js',
                      'plugins/jqvmap.js'
                    ],
    waves:          [
                      '../libs/node-waves/dist/waves.min.css',
                      '../libs/node-waves/dist/waves.min.js',
                      'plugins/waves.js'
                    ]
  };

var MODULE_OPTION_CONFIG = {
  parsley: {
    errorClass: 'is-invalid',
    successClass: 'is-valid',
    errorsWrapper: '<ul class="list-unstyled text-sm mt-1 text-muted"></ul>'
  }
}
