odoo.define('hospital_management.hospitaljs', function (require) {
    'use strict';

    console.log('My Js running')
    
    var publicWidget = require('web.public.widget');

    publicWidget.registry.hospitalWidget = publicWidget.Widget.extend({
        selector: '#hospital_form',
        events: {
            'change .hospital_select': 'hospitalChange',
        },

        hospitalChange: function () {
            //var $wrapwrap = $el.contents().find('div#wrapwrap');
            var hos = $( ".hospital_select option:selected" ).text();
            var hos_id = $( ".hospital_select option:selected" ).val();
            console.log('hospital',hos_id)

            this._rpc({
                route: "/change/hospital",
                params: {
                    hospital_id: parseInt(hos_id),
                    },
            }).then(function (data) {
                console.log("my data", data)
            });
          
        },



        // this._rpc({
        //     route: "/warehouse/qty",
        //     params: {
        //         product_id: p_id,
        //         },
        //     }).then(function (data) {
        //     var data_object = Object.entries(data)
        //     const isEmpty = Object.keys(data).length === 0;
        //     if (!isEmpty) {
        //         var html =
        //         '<table class="
    
        

    });
});
    