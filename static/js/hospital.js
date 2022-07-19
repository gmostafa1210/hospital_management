odoo.define('hospital_management.hospitaljs', function (require) {
    'use strict';
    var publicWidget = require('web.public.widget');

    publicWidget.registry.hospitalWidget = publicWidget.Widget.extend({
        selector: '#hospital_form',
        events: {
            'change .hospital_select': 'hospitalChange',
            'change .department_select': 'departmentChange',
        },

        hospitalChange: function () {
            var hos_id = $( ".hospital_select option:selected" ).val();
            console.log('hospital',hos_id)

            this._rpc({
                route: "/change/hospital",
                params: {
                    hospital_id: parseInt(hos_id),
                    },
            }).then(function (data) {
                var deptHtml = "<option value=''>Please Select department</option>"
                data.map((ob=>{
                    deptHtml += "<option value='"+ob.id +"'> "+ob.name+" </option>"
                }))
                //$('.department_select').append(deptHtml)
                $('.department_select').children().remove().end().append(deptHtml) ;
                $('.doctor_select').children().remove().end().append("<option value=''>Please Select department first</option>") ;
            });
        },

        departmentChange: function () {
            var dep_id = $( ".department_select option:selected" ).val();
            var hos_id = $( ".hospital_select option:selected" ).val();
            this._rpc({
                route: "/change/department",
                params: {
                    department_id: parseInt(dep_id),
                    hospital_id: parseInt(hos_id),
                    },
            }).then(function (data) {
                console.log('department',data)
                var docHtml = "<option value=''>Please Select Doctor</option>"
                data.map((ob=>{
                    docHtml += "<option value='"+ob.id +"'> "+ob.name+" </option>"
                }))
                $('.doctor_select').children().remove().end().append(docHtml) ;
            });
        },


    });
});
    