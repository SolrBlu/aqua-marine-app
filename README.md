# Aqua Marine App

## Overview
Aqua Marine App is a cutting-edge framework combining the simplicity of the Aqua language with the power of Next.js and Strapi. It's designed to streamline web development, making it accessible to developers of all skill levels. 

Yes, Aqua is an abstraction, for Next.js, which itself is an abstraction, for React, and who knows how far down it goes lol :0 (hint: it goes to binary)

We like to think of all the languages, services, and proccesses used for web development as collections of large coral reefs in the ocean, except currently the ocean has no water and you can see every coral reef, making starting out in web dev especially challenging. Aqua fills the ocean, covering the reef, and will keep you afloat and abstract all of the things you don't want to see when you first start programming!

## Purpose 
1. Watch on YT ["I Feel Bad For New Programmers" - ThePrimeTime](https://youtu.be/jL88IAxoYOk?si=FlzOODYpFLRvAsgz&t=36) [0:36-3:44]
2. The problem with motivation being a prerequisite to learning how to program, is that the desired finished product (especially today with all of the amazing tools and tricks devs learn) seem so far out of reach from the perspective of a new programmer, how could they ever get to that level. Even learning React/Next.js never really ends
3. The solution is to create even more abstraction, that's the purpose of code, otherwise, we should all just learn c or better yet binary.
4. The point is most people want control over there website look AND functionality with minimal learning required, and without having to pay for a service like Wix/WordPress/Squarespace/etc.
5. It's about time you can code a website in English, without needing to understand what's going on under the hood... but it's all there if you want too :)

##### Example use cases:
1. You have some experience coding, but maybe frontend is not your expertise and you want a finished product fast, with the option to go in later and learn/update the underlying Next.js code. You can stop using our abstraction at ANY TIME without compromising the underlying code that makes your app work. In fact, you can run [this script] we provide from the root of your AquaMarine project to remove all folders and files related to our abstraction, and you're left with next.js, strapi, an updated package.json, and a much more familiar app structure to continue development.

2. Start a new project and build out the basic layout, git control, and deployment. Once you know the direction you want to go in that may require additional/unique functionality, or you get some traffic to your site, hire a dev to finish/maintain your app

## Components - What you need to learn to publish a website to the www
- **GitHub-version-control**: You're using it :) [Learn More](https://en.wikipedia.org/wiki/GitHub)
- **Aqua-language**: The core language providing a simple syntax to manage frontend and backend operations. You're in the right place to learn more, keep reading!
- **Next.js-framework**: A React-based framework for building web applications. [Learn More](https://nextjs.org/learn-pages-router/foundations/about-nextjs/what-is-nextjs)
- **Strapi-cms/db**: A headless content management system (CMS) that provides backend-only functionalities, making content accessible through a GraphQL or REST API and displayable on any device possible. Essentially, a flexible database. [Learn More](https://strapi.io/about-us)
- **Vercel-hosting/deployment**: Vercel builds a frontend-as-a-service product—they make it easy for engineers to deploy and run the user facing parts of their applications on the web. The company also maintains the Next.js web development framework. [Learn More](https://vercel.com/blog/what-is-vercel)


## Getting Started
### Prerequisites
- Node.js (v18.18.2 or higher)
- npm (v6 or higher)

### Installation
1. Clone the repository:
   ```
   git clone https://github.com/SolrBlu/aqua-marine-app.git
   ```

### Install Dependencies
cd aqua-marine-app
npm install

### Initialize Next.js and Strapi applications
<!-- Instructions for initializing -->

### Usage

Describe how to use the Aqua language and how to run the Next.js and Strapi applications.

### Removing All Aqua Code: CAUTION!

```
# CAUTION!!! Read it all before running script! There is no undo script, besides "cmd + z"
#
#
# Script to copy/paste to your command line and run:

rm -rf aqua-language/ (what else...)

#
# Exactly what folders and files are deleted...
- aqua-language/ (And everything it contains, you've been warned!)
- watch.py
- 
#
# In files that are altered, but not deleted, what is changed...
- Package.json:
  - Scripts:
    - "dev":
      - From: "concurrently \"npm run start-next\" \"python3 -u watch.py\""
      - To: "npm run start-next"
- README.md:
  - From: [The provided Aqua README.md]
  - To: [A blank README.md file to be edited] 
```


### Contributing

We welcome contributions! Please read our Contributing Guide for details.

### License

This project is licensed under the MIT License.

### Contact

Elijah Ally - elijah.ally@solrblu.com
Project Link: https://github.com/SolrBlu/aqua-marine-app
