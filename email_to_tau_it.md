# Email to TAU IT — request to repoint personal homepage subdomain

**To:** TAU IT helpdesk (verify the correct address — engineering faculty IT may handle it faster than the central helpdesk)
**From:** `talraviv@tau.ac.il`
**Subject:** Repointing `talraviv.sites.tau.ac.il` to a new GitHub Pages site

---

Hi,

I'm moving my personal homepage from the TAU Wix site to a self-hosted GitHub Pages site that I'll maintain myself.

- Current: https://www.talraviv.sites.tau.ac.il/
- New: https://tal69.github.io/homepage/

I'd like the existing TAU URL to keep working so that external links and citations don't break. Two ways I see:

1. **DNS CNAME** — point `talraviv.sites.tau.ac.il` (or a new `talraviv.eng.tau.ac.il`) at `tal69.github.io`. I'll then register that hostname as the custom domain on the GitHub repo, and the site will be served at the apex of the TAU URL. (DNS records only support host targets, not paths — the path is resolved on the GitHub side once the hostname is configured.)
2. **HTTP 301 redirect** from the current Wix-hosted page to `https://tal69.github.io/homepage/`, preserving the path so old deep links keep working.

If neither is possible under current policy, replacing the existing page with a one-line stub that links to the new site would also work.

Could you let me know which option you support and what you need from my side? If a `*.eng.tau.ac.il` subdomain is the preferred home for personal pages going forward, I'm happy to move there instead.

Thanks,
Tal Raviv
School of Industrial & Intelligent Systems Engineering
talraviv@tau.ac.il · +972-3-640-6977
