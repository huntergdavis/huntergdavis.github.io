(function() {
    function showResults(results, store) {
        var searchResults = document.getElementById('search-results');
    
        // Function to parse dates in the format "16 November 2012"
        function parseDate(dateStr) {
            var parts = dateStr.split(' ');
            var day = parseInt(parts[0], 10);
            var month = parts[1];
            var year = parseInt(parts[2], 10);
    
            // Map month names to month numbers (0-based index)
            var monthNames = {
                'January': 0,
                'February': 1,
                'March': 2,
                'April': 3,
                'May': 4,
                'June': 5,
                'July': 6,
                'August': 7,
                'September': 8,
                'October': 9,
                'November': 10,
                'December': 11
            };
    
            var monthIndex = monthNames[month];
            return new Date(year, monthIndex, day);
        }
    
        if (results.length) { // If there are results...
            // Sort the results by date (newest to oldest)
            results.sort(function(a, b) {
                var dateA = parseDate(store[a.ref].date);
                var dateB = parseDate(store[b.ref].date);
                return dateB - dateA; // Descending order (newest first)
            });
    
            var appendString = '';
    
            for (var i = 0; i < results.length; i++) {  // Iterate over them and generate HTML
                var item = store[results[i].ref];
                appendString += '<li><a href="' + item.url + '">(' + item.date + ") " + item.title + '</a>';
                appendString += '<p>' + item.content.substring(0, 250) + '...</p></li>';
            }
    
            searchResults.innerHTML = appendString;
        } else {
            searchResults.innerHTML = '<li>No results found</li>';
        }
    }
    
  
    function getQuery(variable) {
      var query = window.location.search.substring(1);
      var vars = query.split('&');
  
      for (var i = 0; i < vars.length; i++) {
        var pair = vars[i].split('=');
  
        if (pair[0] === variable) {
          return decodeURIComponent(pair[1].replace(/\+/g, '%20'));
        }
      }
    }
  
    var searchTerm = getQuery('query');
  
    if (searchTerm) {

      // Initalize lunr.js with the fields to search.
      // The title field is given more weight with the "boost" parameter
      var idx = lunr(function () {
        this.field('id');
        this.field('title', { boost: 10 });
        this.field('author');
        this.field('category');
        this.field('content');
        this.field('date');
  
        for (var key in window.store) { // Add the JSON we generated from the site content to Lunr.js.
          this.add({
            'id': key,
            'title': window.store[key].title,
            'author': window.store[key].author,
            'category': window.store[key].category,
            'content': window.store[key].content,
            'date' : window.store[key].date,
          });
        }
      });
  
      var results = idx.search(searchTerm); // Perform search with Lunr.js
      showResults(results, window.store);
    }
  })();
  