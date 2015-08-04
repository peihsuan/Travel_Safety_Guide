$.getJSON('../country_abbr.json', function(country_abbr) {
    $.getJSON('../boca_gov_notice.json', function(gov_notice) {
        var alert_data = {};
        $.each(gov_notice, function(country, alert_color) {
            if (alert_color === 0 && country_abbr[country]) {
                alert_data[country_abbr[country]] = {
                    'fillKey': 'Gray_alert',
                };
            }
            else if (alert_color == 1 && country_abbr[country]) {
                alert_data[country_abbr[country]] = {
                    'fillKey': 'Yellow_alert',
                };
            }
            else if (alert_color == 2 && country_abbr[country]) {
                alert_data[country_abbr[country]] = {
                    'fillKey': 'Orange_alert',
                };
            }
            else if (alert_color == 3 && country_abbr[country]) {
                alert_data[country_abbr[country]] = {
                    'fillKey': 'Red_alert',
                };
            }
        });

        var map = new Datamap({
            element: document.getElementById('container'),
            fills: {
                Gray_alert: 'Gray',
                Yellow_alert: 'Yellow',
                Orange_alert: 'Orange',
                Red_alert: 'Red',
                defaultFill: 'LightGreen'
            },
            data: alert_data,
        });

    });
});


