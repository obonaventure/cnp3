/* Code from http://blog.mastykarz.nl/jquery-random-filter/ */

jQuery.jQueryRandom = 0;
jQuery.extend(jQuery.expr[":"],
{
    random: function(a, i, m, r) {
        if (i == 0) {
            jQuery.jQueryRandom = Math.floor(Math.random() * r.length);
        };
        return i == jQuery.jQueryRandom;
    }
});
/*
 * <ul>
 *     <li>First</li>
 *     <li>Second</li>
 *     <li>Third</li>
 * </ul>
 * <script type="text/javascript">
 *     $().ready(function() {
 *         alert($("li:random").text());
 *     });
 * </script>
 *
 */
