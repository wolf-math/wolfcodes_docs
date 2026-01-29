---
slug: the-url-object
title: "The URL Object"
authors: Aaron Wolf
sidebar_position: 2
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---


## Overview

The URL object in JavaScript provides a way to work with and manipulate URLs easily. It’s particularly useful when you need to construct, parse, or modify URLs within your code.

Many times template strings are used in order to create URLs in JavaScript. Often this is easy and clear enough, but the URL object is a more robust OOP method of dealing with URLs.

Even OpenWeatherMap.org uses template strings in its documentation: `https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}`

For a URL that is fairly static this is fine, however if you want to make changes to this URL you may want to consider using a URL object. 

```javascript
// Using template strings
const lat = 32.087;
const lon = 34.801;
const apiKey = 'your_api_key';
const url = `https://api.openweathermap.org/data/3.0/onecall?lat=${lat}&lon=${lon}&appid=${apiKey}`;

// Using the URL object
const openWeatherUrl = new URL('https://api.openweathermap.org/data/3.0/onecall');
openWeatherUrl.searchParams.set('lat', lat);
openWeatherUrl.searchParams.set('lon', lon);
openWeatherUrl.searchParams.set('appid', apiKey);
```

## Basic usage
You can create a new URL object by passing a URL string to its constructor.

In this case (as opposed to above) the entire URL is passed in with various parts:

```javascript
const url = new URL('https://example.com:8080/path?query=123#section');
```

## Properties
The URL object has several properties that you can use to access parts of the URL:

- `href`: The full URL as a string.
- `protocol`: The protocol (e.g., `https:`).
- `hostname`: The domain name (e.g., `example.com`).
- `port`: The port number (e.g., `8080`).
- `pathname`: The path following the domain (e.g., `/path`).
- `search`: The query string, including the `?` (e.g., `?query=123`).
- `hash`: The fragment identifier, including the `#` (e.g., `#section`).
- `host`: The hostname and port combined (e.g., `example.com:8080`).
- `origin`: The origin of the URL, which is the protocol, hostname, and port.

```javascript
> const url = new URL('https://example.com:8080/path?query=123#section');
> url.port
'8080'
> url.protocol
'https:'
> url.hostname
'example.com'
> url.pathname
'/path'
> url.search
'?query=123'
> url.hash
'#section'
> url.host
'example.com:8080'
```

These can also be used to change the different parts of the URL?:

```javascript
> url.port = 1234
1234
> url.pathname = "differentpath"
'differentpath'
> url.hostname = "example.org"
'example.org'
> url
URL {
  href: 'https://example.org:1234/differentpath?query=123#section',
  origin: 'https://example.org:1234',
  protocol: 'https:',
  username: '',
  password: '',
  host: 'example.org:1234',
  hostname: 'example.org',
  port: '1234',
  pathname: '/differentpath',
  search: '?query=123',
  searchParams: URLSearchParams { 'query' => '123' },
  hash: '#section'
}
```

## Methods

The URL object also has some methods to help modify and interact with the URL.

For instance a _URL search parameter_ is a key and value pair that informs the API server details to serve a user.

`url.searchParams`: Returns a `URLSearchParams` object, which provides methods to work with query string parameters. 

You can:

- Get a query parameter: `url.searchParams.get('query')`
- Set a query parameter: `url.searchParams.set('query', '456')`
- Delete a query parameter: `url.searchParams.delete('query')`
- Iterate over query parameters:
  ```javascript
  url.searchParams.forEach((value, key) => {
    console.log(key, value);
  });
  ```

The `toString()` method can be used to return the full URL as a string, reflecting any changes made to the properties or query parameters.

## Example with open weather map API

The OpenWeatherMap API documentation can be found [here](https://openweathermap.org/api/one-call-3), although they use a template string let’s use this example with a URL object to build and modify an API request.

```javascript
// get values to interpolate to URL
const apiKey = process.env.openWeatherApiKey || 0
const [lat, lon] = [32.08721095615897, 34.801588162316506]

const openWeatherUrl = new URL("https://api.openweathermap.org")

openWeatherUrl.pathname = "data/3.0/onecall"
openWeatherUrl.searchParams.set('lat',lat)
openWeatherUrl.searchParams.set('lon',lon)

// from the docs
openWeatherUrl.searchParams.set('exclude', 'hourly')

openWeatherUrl.searchParams.set('appid', apiKey)

console.log(openWeatherUrl)
```

output:
```javascript
URL {
  href: 'https://api.openweathermap.org/data/3.0/onecall?lat=32.08721095615897&lon=34.801588162316506&exclude=hourly&appid=0',
  origin: 'https://api.openweathermap.org',
  protocol: 'https:',
  username: '',
  password: '',
  host: 'api.openweathermap.org',
  hostname: 'api.openweathermap.org',
  port: '',
  pathname: '/data/3.0/onecall',
  search: '?lat=32.08721095615897&lon=34.801588162316506&exclude=hourly&appid=0',
  searchParams: URLSearchParams {
    'lat' => '32.08721095615897',
    'lon' => '34.801588162316506',
    'exclude' => 'hourly',
    'appid' => '0' },
  hash: ''
}
```

## Summary
The `URL` object in JavaScript provides a structured way to work with URLs, allowing for easy manipulation and construction of complex URLs. While template strings are simple and effective for static URLs, `URL` objects are ideal for cases where URLs are dynamic or require frequent modifications.
