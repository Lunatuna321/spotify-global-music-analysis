# spotify-global-music-analysis

**Author:** Luna Li  
**Affiliation:** University of Washington · Statistics (Data Science Focus)

> For a quick view of clean code, see [`Spotify_Global_Music_Analysis_LunaLi.py`](./Spotify_Global_Music_Analysis_LunaLi.py)

---

## Project Overview
Analyzed 8,500 Spotify tracks from the **Spotify Global Music Dataset (2009–2025)**  
to identify audio, artist, and temporal factors driving track popularity.

---

## Key Objectives
- Cleaned and transformed raw CSV data using **pandas**  
- Explored numeric relationships with **seaborn** correlation heatmaps  
- Visualized how **duration**, **artist popularity**, and **followers** affect popularity  
- Summarized insights into business-oriented findings:  
  > *Shorter, high-energy tracks from popular artists tend to perform better.*

---

## Tools & Libraries
`Python` · `pandas` · `seaborn` · `matplotlib` · `Jupyter Notebook`

---

## Visualizations
1. **Correlation Heatmap** – relationships between popularity, followers, duration  
2. **Popularity Distribution** – histogram of all 8.5K tracks  
3. **Duration vs. Popularity** – scatter plot illustrating shorter-song trend  

---

## Insights
<div class="my-4 w-full overflow-x-auto">
<table class="min-w-full border-collapse text-sm">
<thead>
<tr>
<th class="whitespace-nowrap border-b border-zinc-200 px-3 py-2 text-left text-xs font-medium text-zinc-900 dark:border-zinc-700 dark:text-zinc-100 sm:px-4 sm:text-sm">Finding</th>
<th class="whitespace-nowrap border-b border-zinc-200 px-3 py-2 text-left text-xs font-medium text-zinc-900 dark:border-zinc-700 dark:text-zinc-100 sm:px-4 sm:text-sm">Description</th>
</tr>
</thead>
<tbody>
<tr class="border-b border-zinc-200 hover:bg-zinc-50 dark:border-zinc-800 dark:hover:bg-zinc-900">
<td class="px-3 py-2 text-xs text-zinc-700 dark:text-zinc-300 sm:px-4 sm:text-base">🎧 Shorter songs</td>
<td class="px-3 py-2 text-xs text-zinc-700 dark:text-zinc-300 sm:px-4 sm:text-base">< 3.5 minutes songs tend to get higher popularity</td>
</tr>
<tr class="border-b border-zinc-200 hover:bg-zinc-50 dark:border-zinc-800 dark:hover:bg-zinc-900">
<td class="px-3 py-2 text-xs text-zinc-700 dark:text-zinc-300 sm:px-4 sm:text-base">⚡ High-energy tracks</td>
<td class="px-3 py-2 text-xs text-zinc-700 dark:text-zinc-300 sm:px-4 sm:text-base">Danceable, energetic tracks dominate in recent years</td>
</tr>
<tr class="border-b border-zinc-200 hover:bg-zinc-50 dark:border-zinc-800 dark:hover:bg-zinc-900">
<td class="px-3 py-2 text-xs text-zinc-700 dark:text-zinc-300 sm:px-4 sm:text-base">👥 Large fan base</td>
<td class="px-3 py-2 text-xs text-zinc-700 dark:text-zinc-300 sm:px-4 sm:text-base">Artist followers strongly correlate with track popularity</td>
</tr>
</tbody>
</table>
</div>

---

## Repository Structure
