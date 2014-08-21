window.App = Ember.Application.create({
    LOG_TRANSITIONS: true
});

App.ApplicationAdapter = DS.DjangoRESTAdapter.extend({
    namespace: 'api',
});

var attr = DS.attr;
App.User = DS.Model.extend({
    username: attr(),
    first_name: attr(),
    last_name: attr(),
});

App.Router.map(function() {
    this.resource("session");
});

App.ApplicationRoute = Ember.Route.extend({
    setupController: function(controller, model) {
        var self = this;
        Ember.$.getJSON('/accounts/auth/').then(function(response) {
            self.controllerFor('session').reset();
            self.controllerFor('session').setCurrentUser(response.user_id);
        });
    }
});


App.SessionController = Ember.ObjectController.extend({
    username: null,
    password: null,
    errorMessage: null,

    reset: function() {
        this.setProperties({
            username: null,
            password: null,
            errorMessage: null,
            model: null
        });
    },

    isAuthenticated: function() {
        return (!Ember.isEmpty(this.get('model')));
    }.property('model'),

    setCurrentUser: function(user_id) {
        if (!Ember.isEmpty(user_id)) {
            var currentUser = this.store.find('user', user_id);
            
            this.set('model', currentUser);
        }
    },

    actions: {
        login: function() {
            var self = this,
                data = this.getProperties('username', 'password');
            $.post('/accounts/auth/', data, null, 'json').then(function(response){
                Ember.run(function(){
                    self.set('errorMessage', response.message);
                    self.setCurrentUser(response.user_id);
                });
            });

        },
        logout: function() {
            $.ajax({url: '/accounts/auth/', type: 'delete'});
            this.reset();
            this.transitionToRoute('index');
        }
    }
});
