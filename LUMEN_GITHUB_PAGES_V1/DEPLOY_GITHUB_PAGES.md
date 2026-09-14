# LVS Website — GitHub Pages Deployment

Copyright © 2026 Wolfgang Netik

## Next step

Publish the first public LVS website directly from the existing repository:

`Askaguel/Lumen`

Expected default project-site URL after activation:

`https://askaguel.github.io/Lumen/`

## Upload

Upload the entire `docs/` folder from this package into the root of the `Lumen` repository.

The resulting repository should contain:

```text
Lumen/
├── README.md
├── LICENSE
├── ...
└── docs/
    ├── index.html
    ├── styles.css
    ├── .nojekyll
    ├── robots.txt
    ├── sitemap.xml
    ├── assets/
    ├── machine/
    └── .well-known/
```

## Enable GitHub Pages

1. Open the `Lumen` repository.
2. Open **Settings**.
3. Select **Pages**.
4. Under **Build and deployment**, choose **Deploy from a branch**.
5. Branch: `main`
6. Folder: `/docs`
7. Save.
8. Wait for the Pages deployment to complete.

GitHub states that a project site normally uses:

`https://<owner>.github.io/<repository>/`

So this project should become available at:

`https://askaguel.github.io/Lumen/`

after successful deployment.

## Important

This package does not itself publish the site.
The URL above is the expected GitHub Pages project URL and becomes real only after Pages is enabled successfully.

## Custom domain — later

Do not upload a placeholder `CNAME` file yet.

When you own a domain:
1. Verify the domain in GitHub.
2. Configure it in repository **Settings → Pages**.
3. Configure the required DNS records at the domain provider.
4. Enable HTTPS.

A custom domain should later replace or redirect the GitHub Pages URL.

## After the website is live

Next commercial step:

1. Verify that `/machine/catalog.json` is reachable.
2. Verify `.well-known/lvs-capabilities.json`.
3. Create the first executable Capability Passport Validator.
4. Deploy the private API runtime separately.
5. Prepare AWS Marketplace seller onboarding.
6. Prepare Google Cloud Marketplace vendor onboarding.

