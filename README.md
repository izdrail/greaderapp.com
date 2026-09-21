# Astro Starter Kit: Minimal

```sh
npm create astro@latest -- --template minimal
```

> 🧑‍🚀 **Seasoned astronaut?** Delete this file. Have fun!

## 🚀 Project Structure

Inside of your Astro project, you'll see the following folders and files:

```text
/
├── public/
├── src/
│   └── pages/
│       └── index.astro
└── package.json
```

Astro looks for `.astro` or `.md` files in the `src/pages/` directory. Each page is exposed as a route based on its file name.

There's nothing special about `src/components/`, but that's where we like to put any Astro/React/Vue/Svelte/Preact components.

Any static assets, like images, can be placed in the `public/` directory.

## 🧞 Commands

All commands are run from the root of the project, from a terminal:

| Command                   | Action                                           |
| :------------------------ | :----------------------------------------------- |
| `npm install`             | Installs dependencies                            |
| `npm run dev`             | Starts local dev server at `localhost:4321`      |
| `npm run build`           | Build your production site to `./dist/`          |
| `npm run preview`         | Preview your build locally, before deploying     |
| `npm run astro ...`       | Run CLI commands like `astro add`, `astro check` |
| `npm run astro -- --help` | Get help using the Astro CLI                     |

## 👀 Want to learn more?

Feel free to check [our documentation](https://docs.astro.build) or jump into our [Discord server](https://astro.build/chat).

## Astro Project Details

This is an Astro.js project that ports the static greaderapp.com site into a modern Astro setup.

### Development
- Run `npm run dev` to start the development server.
- Run `npm run build` to create a static build in the `dist` directory.
- Run `npm run preview` to preview the build locally.

### Structure
- `src/pages/`: Contains the Astro versions of the original `design/*.html` files. They are compiled with `build.format: 'file'` so that the exact paths (like `/pricing.html`) remain functional.
- `src/layouts/`: Contains `BaseLayout.astro`, which includes the global `<head>` section, stylesheets, and vendor scripts to perfectly maintain the original visual design and interactions.
- `public/assets/`: The original `design/assets` are kept intact here to preserve paths.
