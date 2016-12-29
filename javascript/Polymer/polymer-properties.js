/* Polymer web-component called 'component'.
 * Properties type are one of Boolean, Date, Number, String, Array or Object
 */
(function(){
        Polymer({
                is: 'component',

                properties: {
                        data: {
                                type: Array,
                                value: function() {
                                        return [
                                        {
                                                name: "Bob",
                                                activities: []
                                        },
                                        {
                                                name: "Alice",
                                                activities: []
                                        }]
                                }
                        },
                        counter: {
                                type: Number,
                                value: 0
                        }
                }

                ready: function(){}
        })
})()



