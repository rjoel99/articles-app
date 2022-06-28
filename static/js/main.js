$(document).ready(function() {

    $('#article-item').on('click', function() {

        $('#articles-tab').show();
    });

    $('#shoes-details').on('click', function() {

        $('#title-table').html("Detalles de calzados");

        table = $('#articles-table');
        httpRequest('https://articles-app-git-rjoel99-dev.apps.sandbox-m2.ll9k.p1.openshiftapps.com/articles/shoes/details', 'GET', table);
    });

    $('#accessories-details').on('click', function() {

        $('#title-table').html("Detalles de accesorios")

        table = $('#articles-table');
        httpRequest('https://articles-app-git-rjoel99-dev.apps.sandbox-m2.ll9k.p1.openshiftapps.com/articles/accessories/details', 'GET', table);
    });

    $('#clothes-details').on('click', function() {

        $('#title-table').html("Detalles de ropa")

        table = $('#articles-table');
        httpRequest('https://articles-app-git-rjoel99-dev.apps.sandbox-m2.ll9k.p1.openshiftapps.com/articles/clothes/details', 'GET', table);
    });
});


/**
 * Realiza la petición HTTP
 * de manera asíncrona.
 * 
 * @param {*} url 
 * @param {*} method 
 * @param {*} element 
 */
function httpRequest(url, method, element) {

    $.ajax({

        url: url,
        type: method,
        contentType: 'application/json',
        success: function(response) {
            successFunc(response, element);
        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.log(jqXHR);
        }
    });
}

/**
 * Verifica el contenido de la respuesta
 * y si no está vacío, despliega la tabla.
 * 
 * @param {*} response 
 * @param {*} table 
 * @returns 
 */
function successFunc(response, table) {

    if (response == null || response.length == 0) {
        table.empty()
        return;
    } 

    setTable(table, Object.keys(response[0]), response);
}


/**
 * Coloca los valores de la respuesta
 * en una tabla, para después mostrarla.
 * 
 * @param {*} table 
 * @param {*} headers 
 * @param {*} body 
 */
function setTable(table, headers, body) {

	table.empty();


    headerTable = getBeginHeaderTable();

    headers.forEach(e => headerTable += '<th scope="col">' + firstLetterToUpperCase(e) + '</th>');

    headerTable += getEndHeaderTable();
    
    table.append(headerTable);
    
    
    bodyTable = getBeginBodyTable();

    body.forEach(e => bodyTable += '<tr>' + appendRow(Object.values(e)) + '</tr>');
    
    bodyTable += getEndBodyTable();

	table.append(bodyTable)


    table.show();
}

/**
 * Convierte la primera letra de una
 * cadena a mayúscula.
 * 
 * @param {*} str 
 * @returns 
 */
function firstLetterToUpperCase(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
}

/**
 * Agrega contenido a una
 * columna.
 * 
 * @param {*} row 
 * @returns 
 */
function appendRow(row) {
	
	result = '';
	
	row.forEach(e => {
	
		element = e == null ? 'N/A' : e;
		
		result += '<td>' + element + '</td>'
	});
	
	return result;
}


function getBeginHeaderTable() {
    return '<thead><tr>';
}

function getEndHeaderTable() {
    return '</tr></thead>'
}

function getBeginBodyTable() {
    return '<tbody><tr>'
}

function getEndBodyTable() {
    return '</tr></tbody>'
}