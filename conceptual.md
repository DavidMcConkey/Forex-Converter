### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

  > Some important differences are that python is oftentimes for server-side scripting while JavaScript is commonly client-side.(Aka python is more back-end and JS front-end) Another big difference is that python is strongly typed with no implicit conversion between types, while JavaScript is weakly typed.

- Given a dictionary like `{"a": 1, "b": 2}`: , list two ways you
  can try to get a missing key (like "c") _without_ your programming
  crashing.

  > The first method would be using get(), for example print(dictname.get('c','Not found')). The second would be setdefault to avoid an error, where the value being searched for gets set a value if not found.

- What is a unit test?

  > A unit test is a useful testing method which tests individually isolated parts of source code as specificed by the user.

- What is an integration test?

  > Integration tests refer to the testing method of gathering multiple facets of source code and testing them as a group

- What is the role of web application framework, like Flask?

  > Frameworks like flask allow for developers to quickly get started on projects with a very understandable and strong foundation which fulfills the intiial tedium.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

  > Route url is helpful for using the route itself while url query parameters help dive deeper with exact search queries.

- How do you collect data from a URL placeholder parameter using Flask?

> You would be able to specify the desired variable in the app.route and then utilize it in a following function. for example:@app.route('/example/<ex>') And then ex would be able to manipulated like x = ex

- How do you collect data from the query string using Flask?

  > Data from the query string is retrievable with the request.args dictionary.

- How do you collect data from the body of the request using Flask?

  > Data from the body of the request is retrievable with request.form.get()

- What is a cookie and what kinds of things are they commonly used for?

  > A cookie is a piece of data from a web browser that can be retrieved at a later point by the server. Cookies are usually used to carry info from site to site, or within a site likethe visitors name.

- What is the session object in Flask?

  > The session object is built off of cookies and allows the server to store certain variables within the session. It is also encoded in comparison to cookies, making it unaccesible to users.

- What does Flask's `jsonify()` do?

  > Jsonify takes json serializable data and converts it into a json string
