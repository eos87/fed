
/* gettext library */

var catalog = new Array();

function pluralidx(count) { return (count == 1) ? 0 : 1; }
catalog['6 a.m.'] = '6 a.m.';
catalog['Add'] = 'Agregar';
catalog['Available %s'] = '%s Disponibles';
catalog['Calendar'] = 'Calendario';
catalog['Cancel'] = 'Cancelar';
catalog['Choose a time'] = 'Elige una hora';
catalog['Choose all'] = 'Selecciona todos';
catalog['Chosen %s'] = '%s Elegidos';
catalog['Clear all'] = 'Elimina todos';
catalog['Clock'] = 'Reloj';
catalog['Hide'] = 'Esconder';
catalog['January February March April May June July August September October November December'] = 'Enero Febrero Marzo Abril Mayo Junio Julio Agosto Septiembre Octubre Noviembre Diciembre';
catalog['Midnight'] = 'Medianoche';
catalog['Noon'] = 'Mediod\u00eda';
catalog['Now'] = 'Ahora';
catalog['Remove'] = 'Remover';
catalog['S M T W T F S'] = 'D L M M J V S';
catalog['Select your choice(s) and click '] = 'Haz tus elecciones y da click en ';
catalog['Show'] = 'Mostrar';
catalog['Sunday Monday Tuesday Wednesday Thursday Friday Saturday'] = 'Domingo Lunes Martes Mi\u00e9rcoles Jueves Viernes S\u00e1bado';
catalog['Today'] = 'Hoy';
catalog['Tomorrow'] = 'Ma\u00f1ana';
catalog['Yesterday'] = 'Ayer';


function gettext(msgid) {
  var value = catalog[msgid];
  if (typeof(value) == 'undefined') {
    return msgid;
  } else {
    return (typeof(value) == 'string') ? value : value[0];
  }
}

function ngettext(singular, plural, count) {
  value = catalog[singular];
  if (typeof(value) == 'undefined') {
    return (count == 1) ? singular : plural;
  } else {
    return value[pluralidx(count)];
  }
}

function gettext_noop(msgid) { return msgid; }


function interpolate(fmt, obj, named) {
  if (named) {
    return fmt.replace(/%\(\w+\)s/g, function(match){return String(obj[match.slice(2,-2)])});
  } else {
    return fmt.replace(/%s/g, function(match){return String(obj.shift())});
  }
}

/* formatting library */

var formats = new Array();

formats['DATETIME_FORMAT'] = 'j \\de F \\de Y \\a \\l\\a\\s H:i';
formats['DATE_FORMAT'] = 'j \\de F \\de Y';
formats['DECIMAL_SEPARATOR'] = ',';
formats['MONTH_DAY_FORMAT'] = 'j \\de F';
formats['NUMBER_GROUPING'] = '3';
formats['TIME_FORMAT'] = 'H:i:s';
formats['FIRST_DAY_OF_WEEK'] = '1';
formats['TIME_INPUT_FORMATS'] = ['%H:%M:%S', '%H:%M'];
formats['THOUSAND_SEPARATOR'] = '.';
formats['DATE_INPUT_FORMATS'] = ['%d/%m/%Y', '%d/%m/%y'];
formats['YEAR_MONTH_FORMAT'] = 'F \\de Y';
formats['SHORT_DATE_FORMAT'] = 'd/m/Y';
formats['SHORT_DATETIME_FORMAT'] = 'd/m/Y H:i';
formats['DATETIME_INPUT_FORMATS'] = ['%d/%m/%Y %H:%M:%S', '%d/%m/%Y %H:%M', '%d/%m/%y %H:%M:%S', '%d/%m/%y %H:%M'];

function get_format(format_type) {
    var value = formats[format_type];
    if (typeof(value) == 'undefined') {
      return msgid;
    } else {
      return value;
    }
}
